#!/usr/bin/env python3
"""
Abel Skill Benchmark v2 - Futurex-Past Dataset
Uses LLM for question classification and ticker extraction.
"""

import subprocess
import json
import urllib.request
import time
import os
from datasets import load_dataset
from datetime import datetime

ABEL_API_KEY = "YOUR_ABEL_API_KEY"
OPENAI_KEY = "YOUR_OPENAI_API_KEY"

def query_llm(prompt, system="", temperature=0.1):
    url = "https://api.openai.com/v1/chat/completions"
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": temperature
    }).encode()

    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    })

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)[:100]}"


def get_abel_prediction(node_name):
    """Call cap_probe.py to get Abel prediction for a node."""
    cmd = [
        "python3", "/tmp/cap_probe.py",
        "--base-url", "https://cap.abel.ai",
        "--api-key", ABEL_API_KEY,
        "observe", node_name
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data.get("ok") and data.get("status_code") == 200:
                return {
                    "node": node_name,
                    "prediction": data["result"]["prediction"],
                    "drivers": data["result"].get("drivers", [])
                }
    except Exception as e:
        pass
    return None


def llm_classify_and_extract(title, prompt_text):
    """Use LLM to decide if a question is suitable for Abel and extract the node name."""
    classification_prompt = f"""You are an expert at the Abel causal analysis platform. Abel's causal graph contains financial market nodes like stock prices, crypto prices, and commodity prices. Each node is named as {{TICKER}}_close, e.g. AAPL_close, NVDA_close, BTCUSD_close, ETHUSD_close, XAUUSD_close.

Given this question, decide:
1. Is this a financial market prediction question that Abel can help with? Abel can ONLY help with questions about stock prices, crypto prices, commodity prices, or market index values. It CANNOT help with sports, entertainment, politics, weather, book rankings, or any non-financial topic.
2. If yes, what is the most likely Abel node name(s) to query? Use the format TICKER_close. For crypto use the USD pair (e.g. BTCUSD_close). For commodities, use common tickers (e.g. XAUUSD_close for gold, CLUSD_close for crude oil). For stocks, use the stock ticker (e.g. AAPL_close, TSLA_close). For indices, try SPY_close for S&P500, QQQ_close for NASDAQ.

Question title: {title}
Question details: {prompt_text[:500]}

Respond in this exact JSON format (no markdown, no extra text):
{{"suitable": true/false, "reason": "brief reason", "nodes": ["NODE1_close", "NODE2_close"]}}

If not suitable, set nodes to an empty list.
If the question mentions a specific stock/crypto/commodity, include its node.
If you're unsure about the exact node name, include multiple plausible variants (e.g. both "BTC_close" and "BTCUSD_close")."""

    response = query_llm(classification_prompt)
    try:
        response = response.strip()
        if response.startswith("```"):
            response = response.split("\n", 1)[1].rsplit("```", 1)[0]
        return json.loads(response)
    except:
        return {"suitable": False, "reason": "Failed to parse LLM response", "nodes": []}


def llm_as_judge(question, ground_truth, answer):
    judge_prompt = f"""You are an expert judge evaluating answer correctness.

Question: {question}
Ground Truth: {ground_truth}
Answer to evaluate: {answer}

Instructions:
1. Compare the answer to the ground truth
2. Consider if they are semantically equivalent (not exact match)
3. For numerical answers, allow small tolerance
4. For Yes/No or multiple choice, check if the answer aligns

Respond with ONLY ONE WORD:
- "CORRECT" if the answer matches ground truth
- "INCORRECT" if the answer contradicts ground truth
- "UNCERTAIN" if cannot determine

Your judgment:"""

    judgment = query_llm(judge_prompt)
    judgment_clean = judgment.strip().upper()

    if "CORRECT" in judgment_clean and "INCORRECT" not in judgment_clean:
        return True, judgment
    elif "INCORRECT" in judgment_clean:
        return False, judgment
    else:
        return None, judgment


# ============================================================
# Main
# ============================================================

print("=" * 80)
print("Abel Skill Benchmark v2 - Futurex-Past Dataset")
print("LLM-based question classification & ticker extraction")
print("=" * 80)

# Step 1: Load dataset
print("\n[1/6] Loading dataset...")
ds = load_dataset("futurex-ai/Futurex-Past", split="train")
print(f"  Total: {len(ds)} questions")

# Step 2: Download cap_probe.py if needed
print("\n[2/6] Ensuring cap_probe.py is available...")
if not os.path.exists("/tmp/cap_probe.py"):
    print("  Downloading cap_probe.py...")
    url = "https://raw.githubusercontent.com/Abel-ai-causality/Abel-skills/main/causal-abel/scripts/cap_probe.py"
    urllib.request.urlretrieve(url, "/tmp/cap_probe.py")
print("  OK")

# Step 3: Verify Abel API
print("\n[3/6] Verifying Abel API connection...")
test = get_abel_prediction("AAPL_close")
if test:
    print(f"  OK - AAPL_close prediction: {test['prediction']:+.4f}")
else:
    print("  FAIL - Abel API unavailable")
    exit(1)

# Step 4: LLM classification for all 244 questions
print(f"\n[4/6] Classifying all {len(ds)} questions via LLM...")
classifications = []
suitable_count = 0

for i, item in enumerate(ds):
    title = item.get('title', '')
    prompt_text = item.get('prompt', '')

    classification = llm_classify_and_extract(title, prompt_text)
    classification['index'] = i
    classification['title'] = title
    classification['prompt'] = prompt_text
    classification['ground_truth'] = str(item.get('ground_truth'))
    classification['id'] = item.get('id')
    classifications.append(classification)

    if classification.get('suitable'):
        suitable_count += 1

    if (i + 1) % 20 == 0:
        print(f"  Classified {i+1}/{len(ds)} ({suitable_count} suitable so far)")
    time.sleep(0.3)

suitable = [c for c in classifications if c.get('suitable')]
print(f"\n  Classification complete:")
print(f"    Total: {len(ds)}")
print(f"    Suitable for Abel: {len(suitable)}")

print(f"\n  Suitable questions:")
for i, s in enumerate(suitable, 1):
    nodes_str = ", ".join(s.get('nodes', []))
    print(f"    {i:>2}. [{nodes_str:20s}] {s['title'][:50]}")

# Step 5: Run comparison test
print(f"\n[5/6] Running comparison test ({len(suitable)} questions)...")

results = []

for i, q in enumerate(suitable, 1):
    print(f"\n  [{i}/{len(suitable)}] {q['title'][:50]}...")

    result = {
        'id': q['id'],
        'title': q['title'],
        'ground_truth': q['ground_truth'],
        'nodes_tried': q.get('nodes', []),
        'classification_reason': q.get('reason', ''),
    }

    # --- LLM Only ---
    llm_prompt = f"""You are a financial prediction expert. Answer this question concisely:

{q['title']}

Ground truth format: {q['ground_truth']}

Give a clear, specific answer. Be brief (1-2 sentences)."""

    llm_response = query_llm(llm_prompt)
    result['llm_response'] = llm_response

    llm_correct, llm_judge = llm_as_judge(q['title'], q['ground_truth'], llm_response)
    result['llm_correct'] = llm_correct
    result['llm_judge_reason'] = llm_judge

    # --- LLM + Abel ---
    abel_data = None
    for node in q.get('nodes', []):
        abel_data = get_abel_prediction(node)
        if abel_data:
            break

    if abel_data:
        pred = abel_data['prediction']
        drivers = abel_data['drivers']
        direction = "UP" if pred > 0 else "DOWN" if pred < 0 else "FLAT"

        abel_prompt = f"""You are a financial prediction expert with access to Abel's causal market analysis system.

Question: {q['title']}

Abel Causal Graph Analysis:
- Target node: {abel_data['node']}
- Predicted change: {pred:.6f} ({pred:+.2%})
- Direction: {direction}
- Key causal drivers: {', '.join(drivers[:5])}
- Graph version: CausalNodeV2
- Analysis type: Observational prediction with causal drivers

Based on this causal analysis and your expertise, answer the question.

Ground truth format: {q['ground_truth']}

Give a clear, specific answer. Be brief (1-2 sentences). Reference the causal data if relevant."""

        abel_response = query_llm(abel_prompt)
        result['abel_data'] = abel_data
        result['abel_response'] = abel_response

        abel_correct, abel_judge = llm_as_judge(q['title'], q['ground_truth'], abel_response)
        result['abel_correct'] = abel_correct
        result['abel_judge_reason'] = abel_judge

        lm = 'Y' if llm_correct else ('N' if llm_correct is False else '?')
        am = 'Y' if abel_correct else ('N' if abel_correct is False else '?')
        print(f"    Abel node: {abel_data['node']} | pred: {pred:+.4f} | LLM:{lm} Abel:{am}")
    else:
        result['abel_data'] = None
        result['abel_response'] = llm_response
        result['abel_correct'] = llm_correct
        result['abel_judge_reason'] = "No Abel data available"

        tried = ", ".join(q.get('nodes', []))
        lm = 'Y' if llm_correct else ('N' if llm_correct is False else '?')
        print(f"    No Abel data (tried: {tried}) | LLM:{lm}")

    results.append(result)
    time.sleep(0.3)

# Step 6: Summary
print("\n" + "=" * 80)
print("[6/6] Results Summary")
print("=" * 80)

total = len(results)
with_abel = sum(1 for r in results if r['abel_data'])
llm_correct_n = sum(1 for r in results if r['llm_correct'] is True)
llm_incorrect_n = sum(1 for r in results if r['llm_correct'] is False)
llm_uncertain_n = sum(1 for r in results if r['llm_correct'] is None)
abel_correct_n = sum(1 for r in results if r['abel_correct'] is True)
abel_incorrect_n = sum(1 for r in results if r['abel_correct'] is False)
abel_uncertain_n = sum(1 for r in results if r['abel_correct'] is None)

print(f"\nDataset: {len(ds)} total questions")
print(f"Suitable for Abel (LLM-classified): {total}")
print(f"Abel data obtained: {with_abel}/{total} ({with_abel/total*100:.1f}%)")

print(f"\nLLM as Judge Results:")
print(f"  LLM Only:        Correct={llm_correct_n} ({llm_correct_n/total*100:.1f}%)  Incorrect={llm_incorrect_n}  Uncertain={llm_uncertain_n}")
print(f"  LLM + Abel Skill: Correct={abel_correct_n} ({abel_correct_n/total*100:.1f}%)  Incorrect={abel_incorrect_n}  Uncertain={abel_uncertain_n}")

improvement = (abel_correct_n - llm_correct_n) / total * 100 if total else 0
print(f"\n  Accuracy improvement: {improvement:+.1f}%")

improved = [r for r in results if r['llm_correct'] is not True and r['abel_correct'] is True]
worsened = [r for r in results if r['llm_correct'] is True and r['abel_correct'] is not True]

print(f"\n  Cases improved by Abel: {len(improved)}")
for r in improved:
    print(f"    - {r['title'][:60]}")
print(f"  Cases worsened by Abel: {len(worsened)}")
for r in worsened:
    print(f"    - {r['title'][:60]}")

# Save results
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
result_file = f"/Users/zeyu/abel/benchmark_v2_results_{timestamp}.json"

output = {
    'timestamp': timestamp,
    'version': 'v2-llm-classification',
    'total_dataset_questions': len(ds),
    'suitable_questions': total,
    'summary': {
        'abel_data_obtained': with_abel,
        'abel_data_rate': with_abel / total * 100 if total else 0,
        'llm_only_accuracy': llm_correct_n / total * 100 if total else 0,
        'abel_accuracy': abel_correct_n / total * 100 if total else 0,
        'improvement': improvement,
        'improved_count': len(improved),
        'worsened_count': len(worsened),
    },
    'classifications': [{'index': c['index'], 'suitable': c.get('suitable'), 'reason': c.get('reason'), 'nodes': c.get('nodes', []), 'title': c['title']} for c in classifications],
    'results': results,
}

with open(result_file, 'w') as f:
    json.dump(output, f, indent=2, default=str)

print(f"\nFull results saved to: {result_file}")
print("=" * 80)
