from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def material(type_: str, title: str, content: str) -> dict:
    return {"type": type_, "title": title, "content": content}


def option(label: str, text: str) -> dict:
    return {"label": label, "text": text}


DETAILS = {
    "v14d_001": {
        "paired_case_group": "formal_identification_campaign",
        "materials": [
            material(
                "causal_graph",
                "Observed DAG",
                "Nodes: campaign_exposure, site_visits, conversion, seasonality. "
                "Edges: seasonality -> campaign_exposure; seasonality -> conversion; "
                "campaign_exposure -> site_visits; site_visits -> conversion; "
                "campaign_exposure -> conversion. All nodes are observed.",
            ),
            material(
                "document_excerpt",
                "Measurement note",
                "Seasonality is measured before campaigns launch. Site visits are "
                "recorded after campaign exposure and before conversion.",
            ),
        ],
        "options": [
            option("A", "No adjustment is needed."),
            option("B", "Adjust for site_visits only."),
            option("C", "Adjust for seasonality only."),
            option("D", "Adjust for seasonality and site_visits."),
            option("E", "The total effect is not identifiable from observed variables."),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["label", "identified", "adjustment_set", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "C",
                "identified": True,
                "adjustment_set": ["seasonality"],
                "rationale": (
                    "Seasonality is the backdoor confounder. Site_visits lies on the "
                    "causal pathway and should not be adjusted when estimating the "
                    "total effect."
                ),
            },
            "accepted_alternatives": [
                {
                    "adjustment_set": ["seasonality"],
                    "notes": "Equivalent ordering or synonymous wording is acceptable.",
                }
            ],
            "scoring_rubric": {
                "primary_fields": ["label", "identified", "adjustment_set"],
                "field_weights": {
                    "label": 0.25,
                    "identified": 0.25,
                    "adjustment_set": 0.35,
                    "rationale": 0.15,
                },
            },
            "evidence_summary": [
                "seasonality opens the only observed backdoor path",
                "site_visits is a mediator and blocking it would distort the total effect",
            ],
            "common_failure_modes": [
                "adjusting for the mediator",
                "claiming no adjustment is needed because the treatment has a direct edge",
            ],
        },
    },
    "v14d_002": {
        "paired_case_group": "formal_counterfactual_scm",
        "materials": [
            material(
                "causal_graph",
                "SCM graph",
                "Binary variables with edges X -> M -> Y and Z -> Y. No hidden "
                "confounding is assumed.",
            ),
            material(
                "document_excerpt",
                "Structural equations and observations",
                "M := X. Y := M OR Z. Observed facts: X=1, Z=0, therefore M=1 and Y=1.",
            ),
        ],
        "options": [
            option("A", "Yes, Y would still have occurred under do(X=0)."),
            option("B", "No, Y would not have occurred under do(X=0)."),
            option("C", "The counterfactual is not identifiable from the information given."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "counterfactual_outcome", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "counterfactual_outcome": 0,
                "rationale": (
                    "Under do(X=0), M becomes 0. Because Z is observed to be 0, Y = 0 OR "
                    "0 = 0, so Y would not occur."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "counterfactual_outcome"],
                "field_weights": {
                    "label": 0.4,
                    "counterfactual_outcome": 0.4,
                    "rationale": 0.2,
                },
            },
            "evidence_summary": [
                "deterministic SCM supplied",
                "no hidden confounder blocks counterfactual evaluation",
            ],
            "common_failure_modes": [
                "answering from the observed world instead of the intervened world",
                "claiming the case is unidentifiable despite an explicit SCM",
            ],
        },
    },
    "v14d_003": {
        "paired_case_group": "formal_correlation_vs_cause",
        "materials": [
            material(
                "causal_graph",
                "Observed structure",
                "Edges: Z -> X, Z -> Y, X -> M, M -> Y. There is no direct edge X -> Y.",
            ),
            material(
                "table",
                "Association snapshot",
                "Observed data show P(Y=1 | X=1)=0.70 and P(Y=1 | X=0)=0.30.",
            ),
        ],
        "options": [
            option("A", "Supported: X has a causal effect on Y, but only indirectly."),
            option("B", "Unsupported: the graph shows association only, not causation."),
            option("C", "Contradicted: the graph rules out any causal effect from X to Y."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "effect_type", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "A",
                "effect_type": "indirect_causal_effect",
                "rationale": (
                    "X affects Y through the mediator M. The lack of a direct edge does "
                    "not remove the indirect causal path."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "effect_type"],
                "field_weights": {"label": 0.45, "effect_type": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "direct effect absent but indirect path exists",
                "observed association is consistent with both confounding and mediation",
            ],
            "common_failure_modes": [
                "equating no direct edge with no causal effect",
                "equating association alone with sufficient evidence",
            ],
        },
    },
    "v14d_004": {
        "paired_case_group": "graph_mechanism_price_margin",
        "materials": [
            material(
                "causal_graph",
                "Mechanism graph",
                "Edges: price_change -> unit_volume, unit_volume -> freight_cost, "
                "unit_volume -> gross_margin, freight_cost -> gross_margin, "
                "cost_inflation -> freight_cost, cost_inflation -> gross_margin.",
            ),
            material(
                "document_excerpt",
                "Narrative description",
                "Management says the price change first altered unit volume, which then "
                "affected both shipping intensity and margin realization.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["mediator_node", "mechanism_path"],
        },
        "ground_truth": {
            "canonical_answer": {
                "mediator_node": "unit_volume",
                "mechanism_path": ["price_change", "unit_volume", "gross_margin"],
            },
            "accepted_alternatives": [
                {
                    "mechanism_path": [
                        "price_change",
                        "unit_volume",
                        "freight_cost",
                        "gross_margin",
                    ],
                    "notes": "Longer valid paths that still identify unit_volume as the mediator receive full credit.",
                }
            ],
            "scoring_rubric": {
                "primary_fields": ["mediator_node", "mechanism_path"],
                "field_weights": {"mediator_node": 0.6, "mechanism_path": 0.4},
            },
            "evidence_summary": [
                "unit_volume is downstream of price_change and upstream of margin",
                "freight_cost is a later downstream consequence, not the first mediator",
            ],
            "common_failure_modes": [
                "calling freight_cost the mediator",
                "confusing an upstream confounder with an in-path mediator",
            ],
        },
    },
    "v14d_005": {
        "paired_case_group": "graph_path_existence_service_failure",
        "materials": [
            material(
                "causal_graph",
                "Service graph",
                "Edges: supplier_delay -> stockout -> fulfillment_delay -> "
                "customer_complaints -> churn. Also marketing_spend -> new_customers "
                "and price_discount -> new_customers. No arrows lead from marketing_spend "
                "or price_discount into churn through the service chain.",
            )
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["reachable", "example_path", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "reachable": True,
                "example_path": [
                    "supplier_delay",
                    "stockout",
                    "fulfillment_delay",
                    "customer_complaints",
                    "churn",
                ],
                "rationale": "A fully directed service-failure path exists from supplier_delay to churn.",
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["reachable", "example_path"],
                "field_weights": {"reachable": 0.5, "example_path": 0.35, "rationale": 0.15},
            },
            "evidence_summary": [
                "path is directed end to end",
                "irrelevant marketing nodes should not distract from reachability",
            ],
            "common_failure_modes": [
                "reporting no path because the case includes unrelated nodes",
                "providing an undirected or backward path",
            ],
        },
    },
    "v14d_006": {
        "paired_case_group": "graph_encoding_invariance_ads_sales",
        "materials": [
            material(
                "causal_graph",
                "Encoding A: adjacency list",
                "macro_demand -> ad_spend; macro_demand -> sales; ad_spend -> visits; "
                "visits -> sales; promo_discount -> visits; inventory_constraint -> sales.",
            ),
            material(
                "narrative",
                "Encoding B: paragraph",
                "When macro demand strengthens, the company spends more on ads and would "
                "have sold more even without those extra ads. Ads increase visits, and "
                "visits help sales. Promotions also lift visits, while inventory constraints "
                "can cap sales.",
            ),
            material(
                "document_excerpt",
                "Question focus",
                "Identify the node that is the confounder for the relationship between "
                "ad_spend and sales across both encodings.",
            ),
        ],
        "options": [
            option("A", "promo_discount"),
            option("B", "macro_demand"),
            option("C", "inventory_constraint"),
            option("D", "visits"),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "confounder", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "confounder": "macro_demand",
                "rationale": (
                    "Macro demand causes both ad_spend and sales. The answer should stay "
                    "the same under either encoding."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "confounder"],
                "field_weights": {"label": 0.45, "confounder": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "same graph rendered two ways",
                "tests encoding robustness rather than graph memorization",
            ],
            "common_failure_modes": [
                "answering the mediator visits",
                "changing the answer across encodings",
            ],
        },
    },
    "v14d_007": {
        "paired_case_group": "data_vs_text_post_treatment",
        "materials": [
            material(
                "table",
                "Experiment summary",
                "Rows: control, treatment. Columns: assigned_users, conversions, "
                "three_day_engagement_score. The engagement score is measured only after "
                "assignment and after users see the experience.",
            ),
            material(
                "document_excerpt",
                "Metric definitions",
                "Conversion is the primary endpoint. Three-day engagement is computed from "
                "post-assignment behavior inside the product.",
            ),
        ],
        "options": [
            option("A", "Yes. Control for engagement because it predicts conversion."),
            option("B", "No. Engagement is post-treatment and should not be controlled for."),
            option("C", "Yes, but only to improve precision without affecting identification."),
            option("D", "The treatment effect is unidentifiable no matter what is done."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "should_control", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "should_control": False,
                "rationale": (
                    "Three-day engagement is measured after treatment assignment and lies "
                    "on or after the treatment path. Conditioning on it would bias total "
                    "effect estimation."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "should_control"],
                "field_weights": {"label": 0.45, "should_control": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "metric timing is explicit",
                "tests whether the model truly uses the evidence packet",
            ],
            "common_failure_modes": [
                "controlling for a predictive but post-treatment variable",
                "calling the task impossible instead of identifying the trap",
            ],
        },
    },
    "v14d_008": {
        "paired_case_group": "data_grounded_simpson",
        "materials": [
            material(
                "table",
                "Segmented conversion table",
                "Novice users: control 18/100 convert, treatment 15/100 convert. "
                "Expert users: control 70/100 convert, treatment 66/100 convert. "
                "Mixture: treatment traffic is disproportionately expert-heavy, so the "
                "aggregate treatment conversion rate appears higher than the aggregate "
                "control rate.",
            ),
            material(
                "document_excerpt",
                "Assignment note",
                "The treatment was rolled out more aggressively to expert users after a "
                "manual allocation decision.",
            ),
        ],
        "options": [
            option("A", "Treatment helps both overall and within each segment."),
            option("B", "Treatment looks better in aggregate but performs worse within both segments because the traffic mix changed."),
            option("C", "Treatment is worse overall but better within both segments."),
            option("D", "No conclusion can be drawn from the table."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "segment_conclusion", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "segment_conclusion": "simpsons_paradox_due_to_segment_mix",
                "rationale": (
                    "Within both novice and expert strata, treatment underperforms. The "
                    "aggregate improvement is driven by the treated group containing more "
                    "high-converting experts."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "segment_conclusion"],
                "field_weights": {"label": 0.45, "segment_conclusion": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "classic composition effect",
                "mix-shift explanation is explicitly available from the packet",
            ],
            "common_failure_modes": [
                "reporting only the aggregate rate",
                "ignoring the allocation note",
            ],
        },
    },
    "v14d_009": {
        "paired_case_group": "data_grounded_pricing_margin",
        "materials": [
            material(
                "table",
                "Before/after KPI snapshot",
                "List price +2.0%; unit volume -1.0%; input cost per unit -4.0%; gross "
                "margin +3.0 percentage points; competitor prices flat.",
            ),
            material(
                "document_excerpt",
                "Management note",
                "A commodity hedge rolled in during the same quarter and materially reduced "
                "input costs. Management warns that the margin benefit should not be "
                "attributed to pricing alone.",
            ),
        ],
        "options": [
            option("A", "The pricing change clearly caused the full margin expansion."),
            option("B", "The margin expansion cannot be attributed solely to pricing because input costs also moved materially."),
            option("C", "The company must have cut price because volume fell."),
            option("D", "No causal statement of any kind is possible here."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "supportability", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "supportability": "price_not_sufficient_explanation",
                "rationale": (
                    "Pricing and input-cost relief moved at the same time. The packet "
                    "supports a mixed explanation, not a pricing-only causal claim."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "supportability"],
                "field_weights": {"label": 0.45, "supportability": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "competing causal driver explicitly documented",
                "tests supportability rather than blind certainty",
            ],
            "common_failure_modes": [
                "over-claiming that price caused all of the improvement",
                "ignoring the cost hedge note",
            ],
        },
    },
    "v14d_010": {
        "paired_case_group": "narrative_direct_driver_shortage",
        "materials": [
            material(
                "news_packet",
                "Excerpt 1",
                "A typhoon delayed inbound vessels over the weekend and pushed two ocean "
                "arrivals back by roughly three days.",
            ),
            material(
                "news_packet",
                "Excerpt 2",
                "By Tuesday morning, the port said berth congestion had eased and most "
                "containers had been unloaded.",
            ),
            material(
                "news_packet",
                "Excerpt 3",
                "On Tuesday night, a scanner outage at the retailer's regional "
                "distribution center left 40% of inbound pallets unprocessed. Stores ran "
                "out of a promoted SKU the next afternoon.",
            ),
        ],
        "options": [
            option("A", "The typhoon was the most direct driver of the shortage."),
            option("B", "Port congestion was the most direct driver of the shortage."),
            option("C", "The distribution-center scanner outage was the most direct driver of the shortage."),
            option("D", "Seasonal demand was the most direct driver of the shortage."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "direct_driver", "justification"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "C",
                "direct_driver": "distribution_center_scanner_outage",
                "justification": (
                    "Upstream weather mattered earlier, but the packet states that the "
                    "immediate failure before stores stocked out was the scanner outage."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "direct_driver"],
                "field_weights": {"label": 0.45, "direct_driver": 0.35, "justification": 0.20},
            },
            "evidence_summary": [
                "tests direct-driver selection inside a multi-event chain",
                "temporal proximity alone is not enough; the packet names the final bottleneck",
            ],
            "common_failure_modes": [
                "choosing the earliest upstream event",
                "answering with a broad macro story not supported by the excerpts",
            ],
        },
    },
    "v14d_011": {
        "paired_case_group": "narrative_temporal_vs_causal_equity_move",
        "materials": [
            material(
                "news_packet",
                "Excerpt 1",
                "Before market open, the company announced a $2 billion buyback and "
                "raised full-year guidance.",
            ),
            material(
                "news_packet",
                "Excerpt 2",
                "Midday, the CEO appeared on television and repeated the same points from "
                "the morning release without adding new information.",
            ),
            material(
                "news_packet",
                "Excerpt 3",
                "The shares finished the day up 7.8%, with most of the move occurring in "
                "the first 20 minutes after the open.",
            ),
        ],
        "options": [
            option("A", "Yes. The CEO interview was the direct cause of the stock move."),
            option("B", "Unsupported. The buyback and raised guidance are the better-supported drivers, while the interview mostly repeated old information."),
            option("C", "No. Interviews can never cause stock moves."),
            option("D", "The move was random and cannot be analyzed causally."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "causal_read", "justification"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "B",
                "causal_read": "morning_corporate_actions_more_plausible_than_interview",
                "justification": (
                    "The major price move happened before the interview and the interview "
                    "introduced no new information."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "causal_read"],
                "field_weights": {"label": 0.45, "causal_read": 0.35, "justification": 0.20},
            },
            "evidence_summary": [
                "tests temporal-vs-causal confusion",
                "stronger evidence points to the pre-open actions rather than the midday interview",
            ],
            "common_failure_modes": [
                "choosing the later event because it is more salient",
                "making an over-general rule that interviews never matter",
            ],
        },
    },
    "v14d_012": {
        "paired_case_group": "narrative_counterfactual_port_strike",
        "materials": [
            material(
                "news_packet",
                "Excerpt 1",
                "A port strike cut throughput by roughly 25% for five days early in the "
                "month.",
            ),
            material(
                "news_packet",
                "Excerpt 2",
                "Later in the month, heavy rain reduced rail departures by another 10%.",
            ),
            material(
                "news_packet",
                "Excerpt 3",
                "Actual monthly exports ended 18% below plan.",
            ),
        ],
        "options": [
            option("A", "Exports would have finished above plan."),
            option("B", "Exports would have been roughly on plan."),
            option("C", "Exports would still have been below plan, but materially better than realized."),
            option("D", "Exports would have been worse than realized."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "counterfactual_direction", "justification"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "C",
                "counterfactual_direction": "improve_but_remain_below_plan",
                "justification": (
                    "Removing the strike recovers part of the lost throughput, but the "
                    "later rail disruption still leaves exports below plan."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "counterfactual_direction"],
                "field_weights": {
                    "label": 0.45,
                    "counterfactual_direction": 0.35,
                    "justification": 0.20,
                },
            },
            "evidence_summary": [
                "counterfactual must remove one event while keeping the other",
                "tests whether the model avoids all-or-nothing reasoning",
            ],
            "common_failure_modes": [
                "assuming no strike means fully normal month",
                "ignoring the remaining rain shock",
            ],
        },
    },
    "v14d_013": {
        "paired_case_group": "finance_margin_miss",
        "materials": [
            material(
                "document_excerpt",
                "Earnings excerpt",
                "Revenue grew 12% year over year, but operating margin missed consensus. "
                "Management highlighted a larger-than-expected mix shift into lower-margin "
                "hardware and elevated expedited freight costs.",
            ),
            material(
                "table",
                "KPI table",
                "Hardware mix: 46% -> 58%. Services mix: 54% -> 42%. Hardware gross "
                "margin: 24% -> 18%. Services gross margin: 72% -> 70%. Expedited freight "
                "cost as % of revenue: 0.4% -> 2.2%.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["primary_driver", "supporting_variables", "confidence"],
        },
        "ground_truth": {
            "canonical_answer": {
                "primary_driver": "mix_shift_into_lower_margin_hardware_amplified_by_freight",
                "supporting_variables": [
                    "hardware_mix_up",
                    "hardware_gross_margin_down",
                    "expedited_freight_cost_up",
                ],
                "confidence": "medium_high",
            },
            "accepted_alternatives": [
                {
                    "primary_driver": "lower_margin_hardware_mix",
                    "notes": "Answers that foreground mix shift and still cite freight as a "
                    "supporting factor receive full credit.",
                }
            ],
            "scoring_rubric": {
                "primary_fields": ["primary_driver", "supporting_variables"],
                "field_weights": {
                    "primary_driver": 0.45,
                    "supporting_variables": 0.35,
                    "confidence": 0.20,
                },
            },
            "evidence_summary": [
                "revenue growth alone is not a valid margin explanation",
                "packet supports a causal variable relationship between product mix and margin",
            ],
            "common_failure_modes": [
                "answering with generic cost inflation despite no evidence",
                "treating revenue growth itself as the driver of margin miss",
            ],
        },
    },
    "v14d_014": {
        "paired_case_group": "finance_paid_acquisition_cut",
        "materials": [
            material(
                "document_excerpt",
                "Marketing memo",
                "Paid search contributes 62% of first qualified visits, organic contributes "
                "28%, referral contributes 10%. Paid CAC has been rising but remains the "
                "largest controllable volume lever.",
            ),
            material(
                "table",
                "Geo-test results",
                "In prior geo tests, cutting one paid lead generated only 0.25 organic "
                "replacement leads on average within the same month.",
            ),
        ],
        "options": [
            option("A", "Qualified leads would likely drop materially, while CAC improves only partially because organic replacement is limited."),
            option("B", "Qualified leads would stay roughly flat because organic demand will fully replace paid traffic."),
            option("C", "Revenue would rise immediately because paid traffic is always low quality."),
            option("D", "There is no basis for any directional judgment."),
        ],
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": ["label", "base_case", "rationale"],
        },
        "ground_truth": {
            "canonical_answer": {
                "label": "A",
                "base_case": "lead_volume_down_partial_efficiency_gain",
                "rationale": (
                    "The memo and geo test imply incomplete organic substitution. Cutting "
                    "paid acquisition should reduce qualified leads before any efficiency "
                    "benefit fully offsets the loss."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["label", "base_case"],
                "field_weights": {"label": 0.45, "base_case": 0.35, "rationale": 0.20},
            },
            "evidence_summary": [
                "tests business counterfactual reasoning, not ad-tech trivia",
                "geo-test elasticity is the key causal clue",
            ],
            "common_failure_modes": [
                "assuming perfect organic substitution",
                "assuming paid traffic is categorically low quality with no packet support",
            ],
        },
    },
    "v14d_015": {
        "paired_case_group": "finance_dominant_driver",
        "materials": [
            material(
                "document_excerpt",
                "Analyst note",
                "Management cited three factors for the quarter: a one-point constant-currency "
                "headwind, a 40 bps legal reserve, and weaker channel sell-through that "
                "pushed inventory days higher.",
            ),
            material(
                "table",
                "Operating summary",
                "Revenue miss versus plan: -6%. Constant-currency impact: -1 point. Legal "
                "reserve impact on operating margin: -0.4 points. Channel inventory days: "
                "+12 days. End-market sell-through: -9%.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["primary_driver", "supporting_variables", "confidence"],
        },
        "ground_truth": {
            "canonical_answer": {
                "primary_driver": "channel_inventory_correction_and_weak_sell_through",
                "supporting_variables": [
                    "inventory_days_up",
                    "sell_through_down",
                    "revenue_miss_much_larger_than_fx_headwind",
                ],
                "confidence": "medium_high",
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["primary_driver", "supporting_variables"],
                "field_weights": {
                    "primary_driver": 0.45,
                    "supporting_variables": 0.35,
                    "confidence": 0.20,
                },
            },
            "evidence_summary": [
                "dominant driver must explain most of the miss magnitude",
                "FX and legal reserve are too small to be the main answer",
            ],
            "common_failure_modes": [
                "choosing the most familiar macro explanation",
                "overweighting a one-time legal item that mainly affects margin, not revenue",
            ],
        },
    },
    "v14d_016": {
        "paired_case_group": "industrial_identification_temperature",
        "materials": [
            material(
                "operational_log",
                "Process snapshot",
                "Defect rate fell from 4.8% to 3.9% after a temperature-policy increase on "
                "Line A. In the same week, Line A received a maintenance overhaul, while "
                "other lines did not.",
            ),
            material(
                "document_excerpt",
                "Rollout note",
                "The temperature change was applied only on the renovated line. Throughput "
                "also dipped during the same maintenance window.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["identified", "needed_controls", "risk_note"],
        },
        "ground_truth": {
            "canonical_answer": {
                "identified": False,
                "needed_controls": ["maintenance_status", "line_id", "throughput"],
                "risk_note": (
                    "The treatment is confounded by simultaneous maintenance and line "
                    "selection. The observed packet does not support a clean causal estimate."
                ),
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["identified", "needed_controls"],
                "field_weights": {"identified": 0.5, "needed_controls": 0.3, "risk_note": 0.2},
            },
            "evidence_summary": [
                "simultaneous maintenance shift breaks identification",
                "tests supportability rather than blind estimation",
            ],
            "common_failure_modes": [
                "treating before/after deltas as causal proof",
                "ignoring line selection and maintenance timing",
            ],
        },
    },
    "v14d_017": {
        "paired_case_group": "industrial_staggered_rollout",
        "materials": [
            material(
                "operational_log",
                "Plant adoption timeline",
                "Six plants adopted a scheduling policy across four different months. "
                "Pre-rollout output and defect trends are visually similar across plants.",
            ),
            material(
                "document_excerpt",
                "Evaluation task",
                "Leadership wants a design that estimates the policy effect while accounting "
                "for staggered adoption.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["design", "key_assumption", "risk_note"],
        },
        "ground_truth": {
            "canonical_answer": {
                "design": "staggered_difference_in_differences_event_study",
                "key_assumption": "parallel_trends_absent_the_policy",
                "risk_note": "Check for anticipation effects and cross-plant spillovers.",
            },
            "accepted_alternatives": [
                {
                    "design": "event_study_with_staggered_treatment_timing",
                    "notes": "Equivalent design wording receives full credit.",
                }
            ],
            "scoring_rubric": {
                "primary_fields": ["design", "key_assumption"],
                "field_weights": {"design": 0.45, "key_assumption": 0.35, "risk_note": 0.20},
            },
            "evidence_summary": [
                "staggered rollout invites DiD/event-study reasoning",
                "parallel trends is the key identification assumption",
            ],
            "common_failure_modes": [
                "suggesting simple before/after comparison",
                "jumping straight to numeric estimation without naming a design",
            ],
        },
    },
    "v14d_018": {
        "paired_case_group": "industrial_estimation_and_assumptions",
        "materials": [
            material(
                "table",
                "Weighted cohort summary",
                "Adjusted treated mean outcome: 81.2. Adjusted control mean outcome: 78.8. "
                "Estimated average treatment effect after weighting: +2.4 points.",
            ),
            material(
                "document_excerpt",
                "Balance note",
                "Covariates available for adjustment include plant size, shift, baseline "
                "quality score, and operator tenure. Overlap diagnostics are acceptable.",
            ),
        ],
        "response_contract": {
            "format": "structured_json",
            "required_fields": ["estimate", "assumptions", "confidence"],
        },
        "ground_truth": {
            "canonical_answer": {
                "estimate": 2.4,
                "assumptions": [
                    "no_unmeasured_confounding_given_adjusted_covariates",
                    "positivity_or_overlap",
                    "stable_outcome_definition_and_no_interference",
                ],
                "confidence": "medium",
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["estimate", "assumptions"],
                "field_weights": {"estimate": 0.45, "assumptions": 0.35, "confidence": 0.20},
            },
            "evidence_summary": [
                "identification and estimation are scored separately",
                "case explicitly supplies weighted estimate but still requires assumption awareness",
            ],
            "common_failure_modes": [
                "copying the estimate without naming assumptions",
                "inventing unsupported extra assumptions unrelated to the packet",
            ],
        },
    },
    "v14d_019": {
        "paired_case_group": "agentic_frozen_bundle_freight",
        "truth_type_override": "hybrid_structured_review",
        "materials": [
            material(
                "retrieval_bundle",
                "Snippet 1",
                "Ocean carriers announced emergency surcharges after a canal disruption "
                "forced rerouting on several Asia-Europe lanes.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 2",
                "Freight rate indices jumped sharply over the same two-day window, while "
                "retailers said they had not yet repriced goods.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 3",
                "Analysts cautioned that the duration of the rerouting shock remained "
                "unclear and could fade if passage normalizes quickly.",
            ),
        ],
        "response_contract": {
            "format": "short_text_plus_json",
            "required_fields": ["primary_driver", "uncertainty", "evidence_used"],
        },
        "ground_truth": {
            "canonical_answer": {
                "primary_driver": "freight_rate_spike_due_to_canal_disruption_and_rerouting",
                "uncertainty": "how_long_the_disruption_and_surcharges_will_persist",
                "evidence_used": ["Snippet 1", "Snippet 2", "Snippet 3"],
            },
            "accepted_alternatives": [
                {
                    "primary_driver": "rerouting_driven_freight_shock",
                    "notes": "Equivalent concise wording is acceptable if causally aligned.",
                }
            ],
            "scoring_rubric": {
                "primary_fields": ["primary_driver", "uncertainty"],
                "field_weights": {
                    "primary_driver": 0.45,
                    "uncertainty": 0.30,
                    "evidence_used": 0.25,
                },
            },
            "evidence_summary": [
                "tests causal synthesis under freshness-sensitive but frozen evidence",
                "good answers must separate what is likely from what remains unresolved",
            ],
            "common_failure_modes": [
                "summarizing headlines without naming a mechanism",
                "overclaiming a durable earnings effect not supported by the packet",
            ],
        },
    },
    "v14d_020": {
        "paired_case_group": "agentic_event_memo_regional_bank",
        "materials": [
            material(
                "retrieval_bundle",
                "Snippet 1",
                "A regional bank's shares fell after a policy official commented that "
                "deposit competition remains intense for smaller lenders.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 2",
                "The bank's last quarterly filing showed a relatively high share of "
                "interest-bearing deposits and rising funding costs.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 3",
                "A rumor about a capital raise circulated online, but no primary-source "
                "filing or company statement confirmed it.",
            ),
        ],
        "response_contract": {
            "format": "short_text_plus_json",
            "required_fields": ["primary_driver", "next_verification", "uncertainty"],
        },
        "ground_truth": {
            "canonical_answer": {
                "primary_driver": "funding_cost_and_deposit_beta_concern",
                "next_verification": "verify_insured_vs_uninsured_deposit_mix_and_wholesale_funding_dependence",
                "uncertainty": "the_unconfirmed_capital_raise_rumor_should_not_be_treated_as_established_fact",
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["primary_driver", "next_verification"],
                "field_weights": {
                    "primary_driver": 0.40,
                    "next_verification": 0.30,
                    "uncertainty": 0.30,
                },
            },
            "evidence_summary": [
                "tests memo-style causal synthesis with verification discipline",
                "answers should privilege primary-source evidence over rumor",
            ],
            "common_failure_modes": [
                "treating the rumor as the main driver",
                "failing to specify what to verify next",
            ],
        },
    },
    "v14d_021": {
        "paired_case_group": "agentic_conflicting_narratives_biotech",
        "materials": [
            material(
                "retrieval_bundle",
                "Snippet 1",
                "A biotech stock rallied after an FDA advisory panel voted in favor of "
                "its therapy.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 2",
                "Social media accounts also circulated an acquisition rumor, but no "
                "credible outlet confirmed it.",
            ),
            material(
                "retrieval_bundle",
                "Snippet 3",
                "Short interest was elevated heading into the vote, which may have "
                "amplified the magnitude of the move.",
            ),
        ],
        "response_contract": {
            "format": "short_text_plus_json",
            "required_fields": ["primary_driver", "uncertainty", "evidence_used"],
        },
        "ground_truth": {
            "canonical_answer": {
                "primary_driver": "positive_fda_panel_vote_improving_approval_odds",
                "uncertainty": "short_squeeze_dynamics_may_have_amplified_the_move_but_do_not_replace_the_main_causal_event",
                "evidence_used": ["Snippet 1", "Snippet 3"],
            },
            "accepted_alternatives": [],
            "scoring_rubric": {
                "primary_fields": ["primary_driver", "uncertainty"],
                "field_weights": {
                    "primary_driver": 0.45,
                    "uncertainty": 0.30,
                    "evidence_used": 0.25,
                },
            },
            "evidence_summary": [
                "tests selection among competing narratives",
                "main event should outrank unsupported rumor, while magnitude amplification remains a valid uncertainty",
            ],
            "common_failure_modes": [
                "choosing the rumor because it sounds more dramatic",
                "ignoring the distinction between driver and amplifier",
            ],
        },
    },
}


def load_seeds() -> list[dict]:
    data = json.loads((ROOT / "public_dev_seed_set.json").read_text())
    return data["cases"]


def build_cases_and_truth() -> tuple[dict, dict, str]:
    seeds = load_seeds()
    seed_ids = {case["id"] for case in seeds}
    detail_ids = set(DETAILS)
    missing = sorted(seed_ids - detail_ids)
    extra = sorted(detail_ids - seed_ids)
    if missing or extra:
        raise SystemExit(f"Seed/detail mismatch. missing={missing} extra={extra}")

    cases = []
    truths = []
    for seed in sorted(seeds, key=lambda item: item["id"]):
        detail = DETAILS[seed["id"]]
        case_obj = dict(seed)
        if "truth_type_override" in detail:
            case_obj["truth_type"] = detail["truth_type_override"]
        case_obj["authoring_status"] = "instantiated_public_dev"
        case_obj["benchmark_inspirations"] = seed["source_family"]
        case_obj["instantiated_inputs"] = detail["materials"]
        case_obj["response_contract"] = detail["response_contract"]
        if "options" in detail:
            case_obj["options"] = detail["options"]
        if "paired_case_group" in detail:
            case_obj["paired_case_group"] = detail["paired_case_group"]
        cases.append(case_obj)

        truths.append(
            {
                "id": seed["id"],
                "track": seed["track"],
                "truth_type": detail.get("truth_type_override", seed["truth_type"]),
                "canonical_answer": detail["ground_truth"]["canonical_answer"],
                "accepted_alternatives": detail["ground_truth"]["accepted_alternatives"],
                "scoring_rubric": detail["ground_truth"]["scoring_rubric"],
                "evidence_summary": detail["ground_truth"]["evidence_summary"],
                "common_failure_modes": detail["ground_truth"]["common_failure_modes"],
            }
        )

    casebook = {
        "version": "v14-alpha-public-dev-cases",
        "split": "public_dev",
        "case_count": len(cases),
        "notes": [
            "Each case is individually authored and instantiated from the v14 seed set.",
            "This pack is meant for public development and interpretability, not hidden evaluation.",
            "Ground truth is separated into public_dev_ground_truth.json.",
        ],
        "cases": cases,
    }
    ground_truth = {
        "version": "v14-alpha-public-dev-ground-truth",
        "split": "public_dev",
        "case_count": len(truths),
        "notes": [
            "Ground truth remains track-specific and does not force one universal answer format.",
            "Scoring should use the field weights in each case instead of a single scalar-only judge.",
        ],
        "cases": truths,
    }

    lines = ["# v14 Public Dev Cases", "", "| ID | Track | Truth | Title |", "|---|---|---|---|"]
    for case in cases:
        lines.append(
            f"| `{case['id']}` | `{case['track']}` | `{case['truth_type']}` | {case['title']} |"
        )
    markdown = "\n".join(lines) + "\n"
    return casebook, ground_truth, markdown


def main() -> None:
    casebook, ground_truth, markdown = build_cases_and_truth()
    (ROOT / "public_dev_cases.json").write_text(
        json.dumps(casebook, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "public_dev_ground_truth.json").write_text(
        json.dumps(ground_truth, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "public_dev_cases.md").write_text(markdown)
    print("wrote", ROOT / "public_dev_cases.json")
    print("wrote", ROOT / "public_dev_ground_truth.json")
    print("wrote", ROOT / "public_dev_cases.md")


if __name__ == "__main__":
    main()
