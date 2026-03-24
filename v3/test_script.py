#!/usr/bin/env python3
"""
Abel Skill Benchmark v3 - Futurex-Past Dataset
Uses normalize-node for accurate node mapping, traverse-parents for richer context.
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
    """Run cap_probe.py with given subcommand and args."""
    cmd = ["python3", CAP_PROBE, "--base-url", BASE_URL, "--api-key", ABEL_API_KEY] + [subcommand] + list(args)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return json.loads(result.stdout)
    except:
        pass
    return None


def normalize_node(ticker):
    """Use cap_probe normalize-node to get the correct Abel node id."""
    cmd = ["python3", CAP_PROBE, "normalize-node", ticker]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("normalized_node_id", f"{ticker}_close")
    except:
        pass
    return f"{ticker}_close"


def get_abel_data(node):
    """Get prediction + parents for a node."""
    prediction = cap_probe("observe", node)
    parents = cap_probe("traverse-parents", node)

    if prediction and prediction.get("ok") and prediction.get("status_code") == 200:
        result = {
            "node": node,
            "prediction": prediction["result"]["prediction"],
            "drivers": prediction["result"].get("drivers", []),
        }
        if parents and parents.get("ok") and parents.get("status_code") == 200:
            result["parents"] = parents.get("result", {}).get("parents", [])
        return result
    return None


def llm_classify(title, prompt_text):
    """LLM classifies question and extracts candidate tickers."""
    p = f"""You are an expert at financial markets. Given this prediction question, decide:
1. Is this about a specific financial asset (stock, crypto, commodity, index) whose future price/value is being asked?
2. If yes, extract the ticker symbol(s). Use standard market tickers (e.g., AAPL, TSLA, NVDA, BTC, ETH, CL for crude oil, GC for gold, SI for silver, ZS for soybeans, PLTR, LI, OPEN, SPY, DJI, QQQ).

Question: {title}
Details: {prompt_text[:400]}

Respond in JSON only (no markdown):
{{"suitable": true/false, "reason": "brief reason", "tickers": ["TICKER1", "TICKER2"]}}

Rules:
- Sports games (vs, match) are NOT financial, even if team names sound financial.
- Book rankings, movie awards, political events are NOT financial.
- Questions about stock prices, crypto prices, commodity prices, index values ARE financial.
- Extract the ACTUAL asset ticker, not a keyword match."""

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
print("Abel Skill Benchmark v3")
print("normalize-node + traverse-parents + LLM classification")
print("=" * 80)

# 1. Load dataset
print("\n[1/5] Loading dataset...", flush=True)
ds = load_dataset("futurex-ai/Futurex-Past", split="train")
print(f"  Total: {len(ds)} questions", flush=True)

# 2. Verify Abel API + normalize-node
print("\n[2/5] Verifying Abel API...", flush=True)
node = normalize_node("AAPL")
print(f"  normalize-node AAPL -> {node}", flush=True)
test = get_abel_data(node)
if test:
    print(f"  observe {node}: prediction={test['prediction']:+.4f}, drivers={len(test['drivers'])}, parents={len(test.get('parents', []))}", flush=True)
else:
    print("  FAIL", flush=True)
    exit(1)

# 3. Classify all 244 questions
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
        print(f"  {i+1}/{len(ds)} classified ({n} suitable)", flush=True)
    time.sleep(0.25)

suitable = [c for c in classified if c.get('suitable')]
print(f"\n  Result: {len(suitable)} suitable out of {len(ds)}", flush=True)

# 4. For each suitable question: normalize nodes, get abel data, run LLM comparison
print(f"\n[4/5] Running comparison on {len(suitable)} questions...", flush=True)

results = []
for i, q in enumerate(suitable, 1):
    print(f"\n  [{i}/{len(suitable)}] {q['title'][:55]}...", flush=True)

    # Normalize tickers to Abel nodes
    nodes = []
    for t in q.get('tickers', []):
        n = normalize_node(t)
        if n:
            nodes.append(n)
    print(f"    Tickers: {q.get('tickers',[])} -> Nodes: {nodes}", flush=True)

    result = {
        'id': q['id'],
        'title': q['title'],
        'ground_truth': q['ground_truth'],
        'tickers': q.get('tickers', []),
        'nodes': nodes,
        'classification_reason': q.get('reason', ''),
    }

    # --- LLM Only ---
    llm_prompt = f"""You are a financial prediction expert. Answer concisely:

{q['title']}

Expected answer format: {q['ground_truth']}

Give a clear, specific answer in 1-2 sentences."""

    llm_resp = query_llm(llm_prompt)
    result['llm_response'] = llm_resp
    llm_ok, llm_j = llm_judge(q['title'], q['ground_truth'], llm_resp)
    result['llm_correct'] = llm_ok
    result['llm_judge'] = llm_j

    # --- LLM + Abel ---
    abel_data = None
    for n in nodes:
        abel_data = get_abel_data(n)
        if abel_data:
            break

    if abel_data:
        pred = abel_data['prediction']
        drivers = abel_data['drivers']
        parents = abel_data.get('parents', [])
        direction = "UP" if pred > 0 else "DOWN" if pred < 0 else "FLAT"

        parents_str = ""
        if parents:
            parent_names = [p if isinstance(p, str) else p.get('node', str(p)) for p in parents[:8]]
            parents_str = f"\n- Parent nodes (causal drivers from graph): {', '.join(parent_names)}"

        abel_prompt = f"""You are a financial prediction expert with Abel's causal market analysis.

Question: {q['title']}

Abel Causal Graph Analysis:
- Node: {abel_data['node']}
- Predicted change: {pred:.6f} ({pred:+.2%})
- Direction: {direction}
- Key drivers (from observe.predict): {', '.join(drivers[:5])}{parents_str}
- Graph version: CausalNodeV2

Use this causal data to inform your answer. Expected format: {q['ground_truth']}

Give a clear, specific answer in 1-2 sentences. Reference the causal data."""

        abel_resp = query_llm(abel_prompt)
        result['abel_data'] = abel_data
        result['abel_response'] = abel_resp
        abel_ok, abel_j = llm_judge(q['title'], q['ground_truth'], abel_resp)
        result['abel_correct'] = abel_ok
        result['abel_judge'] = abel_j

        lm = 'Y' if llm_ok else ('N' if llm_ok is False else '?')
        am = 'Y' if abel_ok else ('N' if abel_ok is False else '?')
        print(f"    Abel: {abel_data['node']} pred={pred:+.4f} | LLM:{lm} -> Abel:{am}", flush=True)
    else:
        result['abel_data'] = None
        result['abel_response'] = llm_resp
        result['abel_correct'] = llm_ok
        result['abel_judge'] = "No Abel data"
        lm = 'Y' if llm_ok else ('N' if llm_ok is False else '?')
        tried = ", ".join(nodes) if nodes else "none"
        print(f"    No Abel data (tried: {tried}) | LLM:{lm}", flush=True)

    results.append(result)
    time.sleep(0.3)

# 5. Summary
print("\n" + "=" * 80, flush=True)
print("[5/5] Results", flush=True)
print("=" * 80, flush=True)

total = len(results)
with_abel = sum(1 for r in results if r['abel_data'])
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

# Save
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
out = f"/Users/zeyu/abel/benchmark_v3_results_{ts}.json"
with open(out, 'w') as f:
    json.dump({
        'timestamp': ts, 'version': 'v3',
        'total_dataset': len(ds), 'suitable': total,
        'summary': {
            'abel_data_count': with_abel, 'abel_data_rate': with_abel/total*100 if total else 0,
            'llm_accuracy': llm_y/total*100 if total else 0,
            'abel_accuracy': abel_y/total*100 if total else 0,
            'improvement': imp,
            'improved': len(improved), 'worsened': len(worsened),
        },
        'classifications': [{'i': c['index'], 'suitable': c.get('suitable'), 'reason': c.get('reason'), 'tickers': c.get('tickers',[]), 'title': c['title']} for c in classified],
        'results': results,
    }, f, indent=2, default=str)

print(f"\nSaved to: {out}", flush=True)
print("=" * 80, flush=True)
