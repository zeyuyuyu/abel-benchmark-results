#!/usr/bin/env python3
"""
严格按照 Abel-skills repo 规范测试
使用 cap_probe.py + LLM as judge
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
print("严格按照 Abel-skills repo 规范测试")
print("使用 cap_probe.py + LLM as judge")
print("=" * 80)

# 1. 加载数据集
print("\n[1/6] 加载 Futurex-Past 数据集...")
ds = load_dataset("futurex-ai/Futurex-Past", split="train")
print(f"    总共 {len(ds)} 个问题")

# 2. 筛选适合 Abel 的问题
print("\n[2/6] 筛选适合 Abel skill 的问题...")

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
    """提取股票代码 - 严格按照 SKILL.md 规范"""
    text_lower = text.lower()
    for ticker, keywords in FINANCIAL_TICKERS.items():
        for kw in keywords:
            if kw in text_lower:
                return ticker
    return None

def is_strictly_financial(item):
    """严格筛选金融问题 - 按照 SKILL.md When To Use"""
    title = item.get('title', '').lower()
    prompt = item.get('prompt', '').lower()
    text = f"{title} {prompt}"
    
    # 必须有金融关键词
    financial_keywords = [
        'stock', 'price', 'close', 'high', 'low', 'open',
        'trading', 'above', 'below', 'hit', 'index', 'market'
    ]
    
    has_financial = any(kw in text for kw in financial_keywords)
    
    if not has_financial:
        return False, None
    
    # 排除体育
    if ' vs ' in text and any(x in text for x in ['fc ', 'team', 'match', 'winner']):
        return False, None
    
    # 排除娱乐
    if any(x in text for x in ['movie', 'film', 'oscar', 'grammy', 'song']):
        return False, None
    
    # 排除选举
    if any(x in text for x in ['election', 'candidate', 'vote', 'president']):
        return False, None
    
    # 提取股票代码
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

print(f"    找到 {len(suitable_questions)} 个适合 Abel 的问题")
for i, q in enumerate(suitable_questions, 1):
    print(f"      {i}. [{q['ticker']:5s}] {q['title'][:55]}...")

if not suitable_questions:
    print("    没有找到适合的问题！")
    exit(0)

# 3. 使用 cap_probe.py 获取 Abel 数据
print("\n[3/6] 使用 cap_probe.py 获取 Abel 数据...")

def get_abel_prediction(ticker):
    """严格按照 probe-usage.md 使用 cap_probe.py"""
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

# 测试 Abel 连接
print("    测试 Abel API 连接...")
test_result = get_abel_prediction("AAPL")
if test_result:
    print(f"    ✓ Abel API 可用 (AAPL: {test_result['prediction']:+.2%})")
else:
    print(f"    ✗ Abel API 不可用")
    exit(1)

# 4. 定义 LLM 查询函数
print("\n[4/6] 配置 LLM 查询...")

def query_llm(prompt, system=""):
    """查询 OpenAI LLM"""
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

# 5. LLM as judge 函数
print("\n[5/6] 配置 LLM as judge...")

def llm_as_judge(question, ground_truth, answer):
    """使用 LLM 评判答案正确性"""
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

# 6. 运行对比测试
print(f"\n[6/6] 运行对比测试 ({len(suitable_questions)} 个问题)...")
print("    (格式: [LLM→Abel] [Judge: ✓/✗] 问题)")

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
        
        # 严格按照 SKILL.md 构建 prompt
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
        
        llm_mark = '✓' if llm_correct else '✗' if llm_correct is not None else '?'
        abel_mark = '✓' if abel_correct else '✗' if abel_correct is not None else '?'
        
        print(f"      [{llm_mark}→{abel_mark}] Judge: LLM={llm_correct}, Abel={abel_correct}")
    else:
        result['abel_data'] = None
        result['abel_response'] = llm_response
        result['abel_correct'] = llm_correct
        result['abel_judge_reason'] = "No Abel data"
        
        llm_mark = '✓' if llm_correct else '✗' if llm_correct is not None else '?'
        print(f"      [{llm_mark}→-] No Abel data")
    
    results.append(result)
    time.sleep(0.5)

# 7. 统计结果
print("\n" + "=" * 80)
print("7. 测试结果统计")
print("=" * 80)

total = len(results)
llm_correct_count = sum(1 for r in results if r['llm_correct'] is True)
llm_incorrect_count = sum(1 for r in results if r['llm_correct'] is False)
llm_uncertain_count = sum(1 for r in results if r['llm_correct'] is None)

abel_correct_count = sum(1 for r in results if r['abel_correct'] is True)
abel_incorrect_count = sum(1 for r in results if r['abel_correct'] is False)
abel_uncertain_count = sum(1 for r in results if r['abel_correct'] is None)

with_abel_data = sum(1 for r in results if r['abel_data'])

print(f"\n总问题数: {total}")
print(f"获得 Abel 数据: {with_abel_data}/{total} ({with_abel_data/total*100:.1f}%)")

print(f"\nLLM as Judge 评判结果:")
print(f"  LLM Only:")
print(f"    正确: {llm_correct_count} ({llm_correct_count/total*100:.1f}%)")
print(f"    错误: {llm_incorrect_count} ({llm_incorrect_count/total*100:.1f}%)")
print(f"    不确定: {llm_uncertain_count} ({llm_uncertain_count/total*100:.1f}%)")

print(f"\n  LLM + Abel Skill:")
print(f"    正确: {abel_correct_count} ({abel_correct_count/total*100:.1f}%)")
print(f"    错误: {abel_incorrect_count} ({abel_incorrect_count/total*100:.1f}%)")
print(f"    不确定: {abel_uncertain_count} ({abel_uncertain_count/total*100:.1f}%)")

if llm_correct_count + abel_correct_count > 0:
    improvement = (abel_correct_count - llm_correct_count) / total * 100
    print(f"\n  提升: {improvement:+.1f}%")

# 8. 详细案例分析
print("\n" + "=" * 80)
print("8. 详细案例分析")
print("=" * 80)

print("\nA. Abel 改善的案例 (LLM 错误 → Abel 正确):")
improved = [r for r in results if r['llm_correct'] is False and r['abel_correct'] is True]
for i, r in enumerate(improved[:3], 1):
    print(f"\n  {i}. [{r['ticker']}] {r['title'][:50]}...")
    print(f"     Ground Truth: {r['ground_truth']}")
    print(f"     LLM only:     {r['llm_response'][:70]}...")
    print(f"     LLM+Abel:     {r['abel_response'][:70]}...")
    if r['abel_data']:
        print(f"     Abel pred:    {r['abel_data']['prediction']:+.2%}")

print("\nB. Abel 恶化的案例 (LLM 正确 → Abel 错误):")
worsened = [r for r in results if r['llm_correct'] is True and r['abel_correct'] is False]
for i, r in enumerate(worsened[:3], 1):
    print(f"\n  {i}. [{r['ticker']}] {r['title'][:50]}...")
    print(f"     Ground Truth: {r['ground_truth']}")
    print(f"     LLM only:     {r['llm_response'][:70]}...")
    print(f"     LLM+Abel:     {r['abel_response'][:70]}...")

# 9. 保存完整结果
print("\n" + "=" * 80)
print("9. 保存完整结果")
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

print(f"\n完整结果保存至: {result_file}")
print("包含每个 case 的:")
print("  - 问题和 ground truth")
print("  - LLM only 的完整回答")
print("  - LLM + Abel skill 的完整回答")
print("  - Abel 预测数据和驱动因素")
print("  - LLM judge 的评判结果和理由")
print("=" * 80)

if __name__ == "__main__":
    pass  # Script runs when imported or executed
