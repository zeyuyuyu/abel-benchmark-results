#!/usr/bin/env python3
"""
Strict benchmark following Abel-skills repo guidelines.
Uses cap_probe.py + LLM as judge.
"""

import subprocess
import json
import urllib.request
import time
from datasets import load_dataset
from datetime import datetime

# API Keys
API_KEY = "YOUR_ABEL_API_KEY"
OPENAI_KEY = "YOUR_OPENAI_API_KEY"

print("=" * 80)
print("Strict Benchmark Following Abel-skills Repo Guidelines")
print("Uses cap_probe.py + LLM as Judge")
print("=" * 80)

# 1. Load dataset
print("\n[1/6] Loading Futurex-Past dataset...")
ds = load_dataset("futurex-ai/Futurex-Past", split="train")
print(f"    Total: {len(ds)} questions")

# 2. Filter questions suitable for Abel
print("\n[2/6] Filtering questions suitable for Abel skill...")

FINANCIAL_TICKERS = {
    'AAPL': ['aapl', 'apple'],
    'NVDA': ['nvda', 'nvidia'],
    'TSLA': ['tsla', 'tesla'],
    'MSFT': ['msft', 'microsoft'],
    'GOOGL': ['googl', 'google', 'alphabet'],
    'AMZN': ['amzn', 'amazon'],
    'META': ['meta', 'facebook'],
    'BTC': ['btc', 'bitcoin'],
    'SPY': ['spy', 's&p 500', 'sp500'],
    'QQQ': ['qqq', 'nasdaq'],
    'GLD': ['gld', 'gold'],
    'USO': ['uso', 'oil', 'crude'],
}

def extract_ticker(text):
    """Extract ticker symbol - strictly per SKILL.md guidelines"""
    text_lower = text.lower()
    for ticker, keywords in FINANCIAL_TICKERS.items():
        for kw in keywords:
            if kw in text_lower:
                return ticker
    return None

def is_strictly_financial(item):
    """Strict financial question filter - per SKILL.md 'When To Use'"""
    title = item.get('title', '').lower()
    prompt = item.get('prompt', '').lower()
    text = f"{title} {prompt}"

    # Must contain financial keywords
    financial_keywords = [
        'stock', 'price', 'close', 'high', 'low', 'open',
        'trading', 'above', 'below', 'hit', 'index', 'market'
    ]

    has_financial = any(kw in text for kw in financial_keywords)

    if not has_financial:
        return False, None

    # Exclude sports
    if ' vs ' in text and any(x in text for x in ['fc ', 'team', 'match', 'winner']):
        return False, None

    # Exclude entertainment
    if any(x in text for x in ['movie', 'film', 'oscar', 'grammy', 'song']):
        return False, None

    # Exclude elections/politics
    if any(x in text for x in ['election', 'candidate', 'vote', 'president']):
        return False, None

    # Extract ticker
    ticker = extract_ticker(text)

    return ticker is not None, ticker

suitable_questions = []
for item in ds:
    is_suitable, ticker = is_strictly_financial(item)
    if is_suitable:
        suitable_questions.append({
            'id': item.get('id'),
            'title': item.get('title'),
            'prompt': item.get('prompt'),
            'ground_truth': str(item.get('ground_truth')),
            'ticker': ticker
        })

print(f"    Found {len(suitable_questions)} questions suitable for Abel")
for i, q in enumerate(suitable_questions, 1):
    print(f"      {i}. [{q['ticker']:5s}] {q['title'][:55]}...")

if not suitable_questions:
    print("    No suitable questions found!")
    exit(0)

# 3. Fetch Abel data using cap_probe.py
print("\n[3/6] Fetching Abel data via cap_probe.py...")

def get_abel_prediction(ticker):
    """Strictly uses cap_probe.py as per probe-usage.md"""
    cmd = [
        "python3", "/tmp/cap_probe.py",
        "--base-url", "https://cap.abel.ai",
        "--api-key", API_KEY,
        "observe", f"{ticker}_close"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data.get("ok") and data.get("status_code") == 200:
                return {
                    "prediction": data["result"]["prediction"],
                    "drivers": data["result"].get("drivers", [])
                }
    except Exception as e:
        print(f"      Error: {e}")
    return None

# Test Abel connection
print("    Testing Abel API connection...")
test_result = get_abel_prediction("AAPL")
if test_result:
    print(f"    OK - Abel API available (AAPL: {test_result['prediction']:+.2%})")
else:
    print(f"    FAIL - Abel API unavailable")
    exit(1)

# 4. Define LLM query function
print("\n[4/6] Configuring LLM client...")

def query_llm(prompt, system=""):
    """Query OpenAI LLM"""
    url = "https://api.openai.com/v1/chat/completions"

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.1
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
        return f"Error: {str(e)[:50]}"

# 5. LLM as Judge function
print("\n[5/6] Configuring LLM as Judge...")

def llm_as_judge(question, ground_truth, answer):
    """Use LLM to evaluate answer correctness"""
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

    if "CORRECT" in judgment_clean:
        return True, judgment
    elif "INCORRECT" in judgment_clean:
        return False, judgment
    else:
        return None, judgment

# 6. Run comparison test
print(f"\n[6/6] Running comparison test ({len(suitable_questions)} questions)...")
print("    (Format: [LLM->Abel] [Judge: Y/N] Question)")

results = []

for i, q in enumerate(suitable_questions, 1):
    print(f"\n    [{i}/{len(suitable_questions)}] {q['title'][:45]}...")

    result = {
        'id': q['id'],
        'ticker': q['ticker'],
        'title': q['title'],
        'ground_truth': q['ground_truth']
    }

    # 1. LLM Only
    llm_prompt = f"""You are a financial prediction expert. Answer this question concisely:

{q['title']}

Ground truth format: {q['ground_truth']}

Give a clear, specific answer. Be brief (1-2 sentences)."""

    llm_response = query_llm(llm_prompt)
    result['llm_response'] = llm_response

    # Judge LLM only
    llm_correct, llm_judge_reason = llm_as_judge(q['title'], q['ground_truth'], llm_response)
    result['llm_correct'] = llm_correct
    result['llm_judge_reason'] = llm_judge_reason

    # 2. LLM + Abel Skill
    abel_data = get_abel_prediction(q['ticker'])

    if abel_data:
        pred = abel_data['prediction']
        drivers = abel_data['drivers']
        direction = "UP" if pred > 0 else "DOWN" if pred < 0 else "FLAT"

        # Build prompt strictly per SKILL.md
        abel_prompt = f"""You are a financial prediction expert with access to Abel's causal market analysis system.

Question: {q['title']}

Abel Causal Graph Analysis:
- Target node: {q['ticker']}_close
- Predicted change: {pred:.4f} ({pred:+.2%})
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

        # Judge LLM + Abel
        abel_correct, abel_judge_reason = llm_as_judge(q['title'], q['ground_truth'], abel_response)
        result['abel_correct'] = abel_correct
        result['abel_judge_reason'] = abel_judge_reason

        llm_mark = 'Y' if llm_correct else 'N' if llm_correct is not None else '?'
        abel_mark = 'Y' if abel_correct else 'N' if abel_correct is not None else '?'

        print(f"      [{llm_mark}->{abel_mark}] Judge: LLM={llm_correct}, Abel={abel_correct}")
    else:
        result['abel_data'] = None
        result['abel_response'] = llm_response
        result['abel_correct'] = llm_correct
        result['abel_judge_reason'] = "No Abel data"

        llm_mark = 'Y' if llm_correct else 'N' if llm_correct is not None else '?'
        print(f"      [{llm_mark}->-] No Abel data")

    results.append(result)
    time.sleep(0.5)

# 7. Aggregate results
print("\n" + "=" * 80)
print("7. Test Results Summary")
print("=" * 80)

total = len(results)
llm_correct_count = sum(1 for r in results if r['llm_correct'] is True)
llm_incorrect_count = sum(1 for r in results if r['llm_correct'] is False)
llm_uncertain_count = sum(1 for r in results if r['llm_correct'] is None)

abel_correct_count = sum(1 for r in results if r['abel_correct'] is True)
abel_incorrect_count = sum(1 for r in results if r['abel_correct'] is False)
abel_uncertain_count = sum(1 for r in results if r['abel_correct'] is None)

with_abel_data = sum(1 for r in results if r['abel_data'])

print(f"\nTotal questions: {total}")
print(f"Abel data obtained: {with_abel_data}/{total} ({with_abel_data/total*100:.1f}%)")

print(f"\nLLM as Judge Results:")
print(f"  LLM Only:")
print(f"    Correct:   {llm_correct_count} ({llm_correct_count/total*100:.1f}%)")
print(f"    Incorrect: {llm_incorrect_count} ({llm_incorrect_count/total*100:.1f}%)")
print(f"    Uncertain: {llm_uncertain_count} ({llm_uncertain_count/total*100:.1f}%)")

print(f"\n  LLM + Abel Skill:")
print(f"    Correct:   {abel_correct_count} ({abel_correct_count/total*100:.1f}%)")
print(f"    Incorrect: {abel_incorrect_count} ({abel_incorrect_count/total*100:.1f}%)")
print(f"    Uncertain: {abel_uncertain_count} ({abel_uncertain_count/total*100:.1f}%)")

if llm_correct_count + abel_correct_count > 0:
    improvement = (abel_correct_count - llm_correct_count) / total * 100
    print(f"\n  Improvement: {improvement:+.1f}%")

# 8. Detailed case analysis
print("\n" + "=" * 80)
print("8. Detailed Case Analysis")
print("=" * 80)

print("\nA. Cases improved by Abel (LLM incorrect -> Abel correct):")
improved = [r for r in results if r['llm_correct'] is False and r['abel_correct'] is True]
for i, r in enumerate(improved[:3], 1):
    print(f"\n  {i}. [{r['ticker']}] {r['title'][:50]}...")
    print(f"     Ground Truth: {r['ground_truth']}")
    print(f"     LLM only:     {r['llm_response'][:70]}...")
    print(f"     LLM+Abel:     {r['abel_response'][:70]}...")
    if r['abel_data']:
        print(f"     Abel pred:    {r['abel_data']['prediction']:+.2%}")

print("\nB. Cases worsened by Abel (LLM correct -> Abel incorrect):")
worsened = [r for r in results if r['llm_correct'] is True and r['abel_correct'] is False]
for i, r in enumerate(worsened[:3], 1):
    print(f"\n  {i}. [{r['ticker']}] {r['title'][:50]}...")
    print(f"     Ground Truth: {r['ground_truth']}")
    print(f"     LLM only:     {r['llm_response'][:70]}...")
    print(f"     LLM+Abel:     {r['abel_response'][:70]}...")

# 9. Save full results
print("\n" + "=" * 80)
print("9. Saving Full Results")
print("=" * 80)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
result_file = f"/Users/zeyu/abel/strict_test_results_{timestamp}.json"

with open(result_file, 'w') as f:
    json.dump({
        'timestamp': timestamp,
        'total_questions': len(ds),
        'suitable_questions': total,
        'summary': {
            'llm_accuracy': llm_correct_count / total * 100 if total else 0,
            'abel_accuracy': abel_correct_count / total * 100 if total else 0,
            'improvement': (abel_correct_count - llm_correct_count) / total * 100 if total else 0,
            'abel_data_rate': with_abel_data / total * 100 if total else 0,
            'improved_count': len(improved),
            'worsened_count': len(worsened)
        },
        'results': results
    }, f, indent=2, default=str)

print(f"\nFull results saved to: {result_file}")
print("Each case includes:")
print("  - Question and ground truth")
print("  - LLM only complete response")
print("  - LLM + Abel skill complete response")
print("  - Abel prediction data and causal drivers")
print("  - LLM judge evaluation result and reasoning")
print("=" * 80)

if __name__ == "__main__":
    pass
