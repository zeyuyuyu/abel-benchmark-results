# v14 Track G Past-As-Of（Finance 15）A/B 分析

## 1) 评测范围与设置

- 评测集：`track_g_past_asof` 中金融标注子集（15 题，ID 为 `v13ra_001` ~ `v13ra_015`）
- 对比：`codex only` vs `codex + causal-abel skill`
- 评测时间：2026-03-31
- 规则：允许外查，但**每题必须遵守 `search_cutoff`**（as-of 限制）

使用文件：

- 运行摘要：`/Users/zeyu/Documents/bach_private_cache/.bench/v14-track-g-past-asof-results-20260331-101723/summary.json`
- 结果 JSON：`/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v14/track_g_past_asof_results.finance15_20260331.json`
- 结果 Markdown：`/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v14/track_g_past_asof_results.finance15_20260331.md`

## 2) 总体结果（以有效 Case 口径为主）

主口径（公平对比）：

- 仅统计 **双方都给出有效预测** 的 case（去掉空预测与格式无效）
- 有效交集：`13` 题（从 15 题中剔除 `v13ra_006`、`v13ra_007`）

| Run | Correct | Accuracy | Valid Outputs | Duration |
|---|---:|---:|---:|---:|
| codex only | 9/13 | 69.23% | 13/13 | 1344.25s |
| codex + skill | 9/13 | 69.23% | 13/13 | 1625.23s |

结论（本次 15 题）：

- 在“只比较有效 case”的口径下，二者 **持平**（`9/13` vs `9/13`）
- `codex + skill` 更慢（+280.98s）
- 被剔除的 2 题都与空预测/格式问题相关，而不是纯推理差异

补充（原始口径，不剔除无效输出）：

- `codex only`: `10/15 = 66.67%`
- `codex + skill`: `9/15 = 60.00%`

## 3) 分类表现

| Category | Base | Skill |
|---|---:|---:|
| `central_bank_decision` | 4/4 | 4/4 |
| `crypto_binary` | 2/2 | 2/2 |
| `commodity_bucket` | 2/2 | 1/2 |
| `agriculture_bucket` | 1/1 | 1/1 |
| `supply_shock_binary` | 1/1 | 1/1 |
| `commodity_thresholds` | 0/1 | 0/1 |
| `commodity_hit_levels` | 0/1 | 0/1 |
| `first_hit` | 0/2 | 0/2 |
| `single_stock_direction` | 0/1 | 0/1 |

观察：

- 两边都擅长：`central_bank_decision`、`crypto_binary`
- 两边都薄弱：`first_hit`、复杂阈值/命中类题
- 本次唯一明显拉开的是 `commodity_bucket`（skill 因 timeout 少 1 分）

## 4) 关键失分原因（高优先级）

### A. Skill 侧超时导致空答案（直接掉分）

- `v13ra_007`：skill 预测 `None`（batch 5 timeout）
- `v13ra_006`：skill 预测 `None`（batch 6 timeout）

这两题里，`v13ra_006` 本来 base 是答对的（`\boxed{E}`），因此 skill 侧超时造成了净损失。

### B. 格式不合规导致无效（即使语义接近也记错）

- `v13ra_007`（base）输出 `\boxed{BCGJ}`，未按要求使用逗号分隔，判定无效
- 这类格式错误在严格 benchmark 里会直接损失有效率和准确率

### C. 多选阈值题本身难度较高

- `v13ra_005`（commodity_thresholds）：
  - GT: `\boxed{H, I, J, K, L}`
  - base: `\boxed{H}`（漏选）
  - skill: `\boxed{F}`（偏离）
- 体现的是“多标签边界题”对检索+映射能力的压力，而不是单一二分类能力问题。

## 5) Case-level 差异摘要

- **被有效口径剔除**：`v13ra_006`（skill 空预测）、`v13ra_007`（base 格式无效 + skill 空预测）
- **Base-only 正确（原始口径）**：`v13ra_006`
- **Skill-only 正确**：无
- **双方都错**：`v13ra_005`, `v13ra_007`, `v13ra_009`, `v13ra_010`, `v13ra_015`
- 预测发生变化的题：3 题（其中 2 题变化由 skill timeout 引起）

## 6) 解释口径（避免误读）

这 15 题在有效口径下是 `9/13` 对 `9/13`，说明两边“有有效输出时”的答题质量接近。  
原始口径下 skill 落后，主要是工程稳定性（timeout）和输出合规问题造成，而不是显著的推理能力差距。

## 7) 下一步建议

1. 先修稳定性：对 skill run 开启重试或更长超时，先消灭 `None` 预测。
2. 修格式层：统一后处理，强制把 `\boxed{BCGJ}` 规范化为 `\boxed{B, C, G, J}`。
3. 再做公平复测：在“0 timeout + 格式全有效”条件下复跑同一 15 题，才更能代表 skill 的真实增益/损失。
