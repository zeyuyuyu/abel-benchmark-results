#!/usr/bin/env python3
"""
Abel Skill Benchmark v4 - Full skill usage
Uses observe + neighbors + markov-blanket for rich causal context.
"""

import subprocess
import json
import urllib.request
import time
import sys
from datasets import load_dataset
from datetime import datetime

ABEL_API_KEY = "YOUR_ABEL_API_KEY"
OPENAI_KEY = "YOUR_OPENAI_API_KEY"
CAP_PROBE = "/Users/zeyu/abel/Abel-skills/causal-abel/scripts/cap_probe.py"
BASE_URL = "https://cap.abel.ai"

sys.stdout.reconfigure(line_buffering=True)

def query_llm(prompt, system="", temperature=0.1):
    url = "https://api.openai.com/v1/chat/completions"
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    payload = json.dumps({"model": "gpt-4o-mini", "messages": messages, "temperature": temperature}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)[:100]}"


def cap_probe(subcommand, *args):
    cmd = ["python3", CAP_PROBE, "--base-url", BASE_URL, "--api-key", ABEL_API_KEY] + [subcommand] + list(args)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return json.loads(result.stdout)
    except:
        pass
    return None


def normalize_node(ticker):
    cmd = ["python3", CAP_PROBE, "normalize-node", ticker]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("normalized_node_id", f"{ticker}_close")
    except:
        pass
    return f"{ticker}_close"


def get_full_abel_context(node):
    """Get rich causal context: observe + neighbors(parents) + markov-blanket."""
    # 1. Observational prediction
    obs = cap_probe("observe", node)
    if not obs or not obs.get("ok") or obs.get("status_code") != 200:
        return None

    context = {
        "node": node,
        "prediction": obs["result"]["prediction"],
        "drivers": obs["result"].get("drivers", []),
        "parents": [],
        "markov_blanket": [],
    }

    # 2. Neighbors (parents) - structural causal parents
    nbr = cap_probe("neighbors", node, "--scope", "parents", "--max-neighbors", "10")
    if nbr and nbr.get("ok"):
        context["parents"] = [n["node_id"] for n in nbr.get("result", {}).get("neighbors", [])]

    # 3. Markov blanket - full causal neighborhood
    mb = cap_probe("markov-blanket", node, "--max-neighbors", "15")
    if mb and mb.get("ok"):
        blanket = mb.get("result", {}).get("neighbors", [])
        context["markov_blanket"] = [
            {"node": n["node_id"], "role": n["roles"][0] if n.get("roles") else "unknown"}
            for n in blanket
        ]
        context["blanket_total"] = mb.get("result", {}).get("total_candidate_count", 0)

    return context


def build_abel_prompt(question, ground_truth, ctx):
    """Build a rich prompt using full causal context per SKILL.md guidelines."""
    pred = ctx["prediction"]
    direction = "UP" if pred > 0 else "DOWN" if pred < 0 else "FLAT"

    parents_str = ", ".join(ctx["parents"]) if ctx["parents"] else "none identified"

    blanket_parts = []
    for entry in ctx["markov_blanket"][:10]:
        blanket_parts.append(f'{entry["node"]} ({entry["role"]})')
    blanket_str = ", ".join(blanket_parts) if blanket_parts else "not available"

    return f"""You are a financial prediction expert with access to Abel's causal market analysis system.

Question: {question}

Abel Causal Graph Analysis for {ctx['node']}:

1. Observational Prediction (observe.predict):
   - Predicted change: {pred:.6f} ({pred:+.2%})
   - Direction: {direction}
   - Key prediction drivers: {', '.join(ctx['drivers'][:5])}

2. Structural Parents (graph.neighbors scope=parents):
   - Direct causal parents: {parents_str}
   - These are the nodes that directly cause changes in {ctx['node']}

3. Markov Blanket (graph.markov_blanket):
   - Full causal neighborhood ({ctx.get('blanket_total', '?')} total nodes): {blanket_str}
   - Parents cause changes, children are affected, spouses share children

4. Graph Metadata:
   - Graph: CausalNodeV2 (11,315 nodes, 42M+ edges)
   - Algorithm: PCMCI
   - Temporal resolution: 1 hour

Important: The prediction is a short-term (next-period) observational forecast. For longer-horizon questions, consider the structural relationships (parents, blanket) as context for directional reasoning rather than relying solely on the point prediction.

Expected answer format: {ground_truth}
Give a clear, specific answer in 1-2 sentences. Use the causal structure to inform your reasoning."""


def llm_classify(title, prompt_text):
    p = f"""Given this prediction question, decide:
1. Is this about a specific financial asset (stock, crypto, commodity, index) whose future price/value is being asked?
2. If yes, extract the ticker symbol(s).

Question: {title}
Details: {prompt_text[:400]}

Respond in JSON only (no markdown):
{{"suitable": true/false, "reason": "brief reason", "tickers": ["TICKER1"]}}

Rules:
- Sports, book rankings, movie awards, political events = NOT financial.
- Stock prices, crypto, commodity prices, index values = financial.
- Use standard tickers: AAPL, TSLA, NVDA, BTC, CL, GC, SI, ZS, PLTR, LI, OPEN, SPY, DJI, QQQ, PL, PD, etc."""

    response = query_llm(p)
    try:
        response = response.strip()
        if response.startswith("```"):
            response = response.split("\n", 1)[1].rsplit("```", 1)[0]
        return json.loads(response)
    except:
        return {"suitable": False, "reason": "Parse error", "tickers": []}


def llm_judge(question, ground_truth, answer):
    p = f"""You are an expert judge evaluating answer correctness.

Question: {question}
Ground Truth: {ground_truth}
Answer: {answer}

Compare the answer to ground truth. Consider semantic equivalence, small numerical tolerance, and directional alignment.

Respond with ONLY ONE WORD: "CORRECT", "INCORRECT", or "UNCERTAIN"."""

    j = query_llm(p).strip().upper()
    if "INCORRECT" in j:
        return False, j
    elif "CORRECT" in j:
        return True, j
    return None, j


# ============================================================
print("=" * 80)
print("Abel Skill Benchmark v4 - Full Skill Usage")
print("observe + neighbors + markov-blanket for rich causal context")
print("=" * 80)

# 1. Load
print("\n[1/5] Loading dataset...", flush=True)
ds = load_dataset("futurex-ai/Futurex-Past", split="train")
print(f"  Total: {len(ds)} questions", flush=True)

# 2. Verify
print("\n[2/5] Verifying Abel API with full context...", flush=True)
node = normalize_node("NVDA")
ctx = get_full_abel_context(node)
if ctx:
    print(f"  Node: {ctx['node']}", flush=True)
    print(f"  Prediction: {ctx['prediction']:+.4f}", flush=True)
    print(f"  Drivers: {ctx['drivers']}", flush=True)
    print(f"  Parents: {ctx['parents']}", flush=True)
    print(f"  Blanket: {len(ctx['markov_blanket'])} nodes (total: {ctx.get('blanket_total', '?')})", flush=True)
else:
    print("  FAIL", flush=True)
    exit(1)

# 3. Classify
print(f"\n[3/5] Classifying {len(ds)} questions...", flush=True)
classified = []
for i, item in enumerate(ds):
    title = item.get('title', '')
    prompt_text = item.get('prompt', '')
    c = llm_classify(title, prompt_text)
    c['index'] = i
    c['title'] = title
    c['prompt'] = prompt_text
    c['ground_truth'] = str(item.get('ground_truth'))
    c['id'] = item.get('id')
    classified.append(c)
    if (i + 1) % 20 == 0:
        n = sum(1 for x in classified if x.get('suitable'))
        print(f"  {i+1}/{len(ds)} ({n} suitable)", flush=True)
    time.sleep(0.25)

suitable = [c for c in classified if c.get('suitable')]
print(f"\n  Result: {len(suitable)} suitable out of {len(ds)}", flush=True)
for i, s in enumerate(suitable, 1):
    print(f"    {i}. [{','.join(s.get('tickers',[]))}] {s['title'][:55]}", flush=True)

# 4. Run comparison
print(f"\n[4/5] Running comparison ({len(suitable)} questions)...", flush=True)

results = []
for i, q in enumerate(suitable, 1):
    print(f"\n  [{i}/{len(suitable)}] {q['title'][:55]}...", flush=True)

    nodes = [normalize_node(t) for t in q.get('tickers', [])]

    result = {
        'id': q['id'], 'title': q['title'], 'ground_truth': q['ground_truth'],
        'tickers': q.get('tickers', []), 'nodes': nodes,
    }

    # LLM Only
    llm_resp = query_llm(f"""You are a financial prediction expert. Answer concisely:

{q['title']}

Expected answer format: {q['ground_truth']}

Give a clear, specific answer in 1-2 sentences.""")
    result['llm_response'] = llm_resp
    llm_ok, llm_j = llm_judge(q['title'], q['ground_truth'], llm_resp)
    result['llm_correct'] = llm_ok
    result['llm_judge'] = llm_j

    # LLM + Abel (full context)
    abel_ctx = None
    for n in nodes:
        abel_ctx = get_full_abel_context(n)
        if abel_ctx:
            break

    if abel_ctx:
        abel_prompt = build_abel_prompt(q['title'], q['ground_truth'], abel_ctx)
        abel_resp = query_llm(abel_prompt)
        result['abel_context'] = {
            'node': abel_ctx['node'],
            'prediction': abel_ctx['prediction'],
            'drivers': abel_ctx['drivers'],
            'parents': abel_ctx['parents'],
            'blanket_count': len(abel_ctx['markov_blanket']),
            'blanket_total': abel_ctx.get('blanket_total', 0),
        }
        result['abel_response'] = abel_resp
        abel_ok, abel_j = llm_judge(q['title'], q['ground_truth'], abel_resp)
        result['abel_correct'] = abel_ok
        result['abel_judge'] = abel_j

        lm = 'Y' if llm_ok else ('N' if llm_ok is False else '?')
        am = 'Y' if abel_ok else ('N' if abel_ok is False else '?')
        p = abel_ctx['prediction']
        print(f"    {abel_ctx['node']}: pred={p:+.4f}, parents={len(abel_ctx['parents'])}, blanket={len(abel_ctx['markov_blanket'])}", flush=True)
        print(f"    LLM:{lm} -> Abel:{am}", flush=True)
    else:
        result['abel_context'] = None
        result['abel_response'] = llm_resp
        result['abel_correct'] = llm_ok
        result['abel_judge'] = "No Abel data"
        lm = 'Y' if llm_ok else ('N' if llm_ok is False else '?')
        print(f"    No Abel data (tried: {', '.join(nodes)}) | LLM:{lm}", flush=True)

    results.append(result)
    time.sleep(0.3)

# 5. Summary
print("\n" + "=" * 80, flush=True)
print("[5/5] Results", flush=True)
print("=" * 80, flush=True)

total = len(results)
with_abel = sum(1 for r in results if r['abel_context'])
llm_y = sum(1 for r in results if r['llm_correct'] is True)
llm_n = sum(1 for r in results if r['llm_correct'] is False)
llm_q = sum(1 for r in results if r['llm_correct'] is None)
abel_y = sum(1 for r in results if r['abel_correct'] is True)
abel_n = sum(1 for r in results if r['abel_correct'] is False)
abel_q = sum(1 for r in results if r['abel_correct'] is None)

print(f"\nDataset: {len(ds)} total | Suitable: {total} | Abel data: {with_abel} ({with_abel/total*100:.0f}%)", flush=True)
print(f"\nLLM Only:  Correct={llm_y} ({llm_y/total*100:.1f}%)  Incorrect={llm_n}  Uncertain={llm_q}", flush=True)
print(f"LLM+Abel:  Correct={abel_y} ({abel_y/total*100:.1f}%)  Incorrect={abel_n}  Uncertain={abel_q}", flush=True)

imp = (abel_y - llm_y) / total * 100 if total else 0
print(f"Improvement: {imp:+.1f}%", flush=True)

improved = [r for r in results if r['llm_correct'] is not True and r['abel_correct'] is True]
worsened = [r for r in results if r['llm_correct'] is True and r['abel_correct'] is not True]
print(f"\nImproved by Abel ({len(improved)}):", flush=True)
for r in improved:
    print(f"  + {r['title'][:65]}", flush=True)
print(f"Worsened by Abel ({len(worsened)}):", flush=True)
for r in worsened:
    print(f"  - {r['title'][:65]}", flush=True)

# Only-Abel-data cases comparison
print(f"\n--- Cases with Abel data only ({with_abel}) ---", flush=True)
abel_llm_y = sum(1 for r in results if r['abel_context'] and r['llm_correct'] is True)
abel_abel_y = sum(1 for r in results if r['abel_context'] and r['abel_correct'] is True)
if with_abel:
    print(f"LLM Only:  {abel_llm_y}/{with_abel} ({abel_llm_y/with_abel*100:.1f}%)", flush=True)
    print(f"LLM+Abel:  {abel_abel_y}/{with_abel} ({abel_abel_y/with_abel*100:.1f}%)", flush=True)

ts = datetime.now().strftime("%Y%m%d_%H%M%S")
out = f"/Users/zeyu/abel/benchmark_v4_results_{ts}.json"
with open(out, 'w') as f:
    json.dump({
        'timestamp': ts, 'version': 'v4-full-skill',
        'total_dataset': len(ds), 'suitable': total,
        'summary': {
            'abel_data_count': with_abel, 'abel_data_rate': with_abel/total*100 if total else 0,
            'llm_accuracy': llm_y/total*100 if total else 0,
            'abel_accuracy': abel_y/total*100 if total else 0,
            'improvement': imp,
            'improved': len(improved), 'worsened': len(worsened),
            'abel_only_llm_acc': abel_llm_y/with_abel*100 if with_abel else 0,
            'abel_only_abel_acc': abel_abel_y/with_abel*100 if with_abel else 0,
        },
        'results': results,
    }, f, indent=2, default=str)

print(f"\nSaved to: {out}", flush=True)
print("=" * 80, flush=True)
