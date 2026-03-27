from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES_PATH = ROOT / "causal_proxy_intervention_cases.json"
GROUND_TRUTH_PATH = ROOT / "causal_proxy_intervention_ground_truth.json"
MARKDOWN_PATH = ROOT / "causal_proxy_intervention_cases.md"


def material(type_: str, title: str, content: str) -> dict:
    return {"type": type_, "title": title, "content": content}


def option(label: str, text: str) -> dict:
    return {"label": label, "text": text}


def make_case(
    *,
    case_id: str,
    track: str,
    source_family: list[str],
    task_family: str,
    generation_pipeline: str,
    prompt_style: str,
    title: str,
    scenario: str,
    question: str,
    truth_type: str,
    skills_required: list[str],
    slice_tags: list[str],
    inputs: list[dict],
    options: list[dict],
    response_fields: list[str],
    canonical_answer: dict,
    evidence_summary: list[str],
    common_failure_modes: list[str],
    benchmark_inspirations: list[str] | None = None,
    scoring_focus: list[str] | None = None,
    accepted_alternatives: list[dict] | None = None,
    paired_case_group: str | None = None,
    mode_compatibility: list[str] | None = None,
    field_weights: dict[str, float] | None = None,
) -> dict:
    if benchmark_inspirations is None:
        benchmark_inspirations = source_family
    if scoring_focus is None:
        scoring_focus = ["field_level_accuracy"]
    if accepted_alternatives is None:
        accepted_alternatives = []
    if mode_compatibility is None:
        mode_compatibility = ["model_only", "open_book", "tool_agent"]
    if field_weights is None:
        remaining = max(0.0, 1.0 - 0.45)
        other_fields = [field for field in response_fields if field != "label"]
        if other_fields:
            even = round(remaining / len(other_fields), 4)
            field_weights = {"label": 0.45, **{field: even for field in other_fields}}
        else:
            field_weights = {"label": 1.0}

    case = {
        "id": case_id,
        "split": "public_dev",
        "track": track,
        "source_family": source_family,
        "task_family": task_family,
        "generation_pipeline": generation_pipeline,
        "prompt_style": prompt_style,
        "title": title,
        "scenario": scenario,
        "question": question,
        "inputs_needed": [
            {
                "type": item["type"],
                "description": item["title"],
                "required": True,
            }
            for item in inputs
        ],
        "truth_type": truth_type,
        "mode_compatibility": mode_compatibility,
        "skills_required": skills_required,
        "slice_tags": slice_tags,
        "expected_output_schema": {
            "format": "multiple_choice_plus_json",
            "required_fields": response_fields,
            "abstention_allowed": True,
        },
        "scoring_focus": scoring_focus,
        "authoring_status": "instantiated_public_dev",
        "benchmark_inspirations": benchmark_inspirations,
        "instantiated_inputs": inputs,
        "response_contract": {
            "format": "multiple_choice_plus_json",
            "required_fields": response_fields,
        },
        "options": options,
    }
    if paired_case_group:
        case["paired_case_group"] = paired_case_group

    ground_truth = {
        "id": case_id,
        "track": track,
        "truth_type": truth_type,
        "canonical_answer": canonical_answer,
        "accepted_alternatives": accepted_alternatives,
        "scoring_rubric": {
            "primary_fields": response_fields,
            "field_weights": field_weights,
        },
        "evidence_summary": evidence_summary,
        "common_failure_modes": common_failure_modes,
    }

    return {"case": case, "ground_truth": ground_truth}


PACK_CASES = [
    make_case(
        case_id="v14cpi_001",
        track="finance_and_business_causal_reasoning",
        source_family=["XFinBench", "FinBen", "Finance Agent"],
        task_family="proxy_family_selection",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="analyst_memo",
        title="Homebuilder Miss: Funding Stress Or Demand Softness?",
        scenario="A morning note combines mortgage data, builder credit signals, order metrics, and website activity after a homebuilder stock selloff.",
        question="Which proxy family should you prioritize to explain the move, and what evidence would most directly falsify that read?",
        truth_type="hybrid_structured_review",
        skills_required=["proxy_routing", "event_reasoning", "falsification"],
        slice_tags=["finance", "proxy_routing", "financing_conditions", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Morning note",
                "The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.",
            ),
            material(
                "table",
                "Market and operating snapshot",
                "30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.",
            ),
        ],
        options=[
            option("A", "Financing conditions and mortgage affordability are the cleaner proxy family."),
            option("B", "End-demand collapse is the cleaner proxy family."),
            option("C", "Land-supply constraints are the cleaner proxy family."),
            option("D", "Accounting noise is the cleaner proxy family."),
        ],
        response_fields=["label", "primary_proxy_family", "falsifier"],
        canonical_answer={
            "label": "A",
            "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
            "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize",
        },
        evidence_summary=[
            "Mortgage affordability worsened materially while traffic and visits stayed roughly intact.",
            "Credit and rate signals moved sharply, which fits hesitation around financing more than collapse in underlying shopper interest.",
        ],
        common_failure_modes=[
            "Treating a modest cancellation increase as proof of broad demand collapse.",
            "Ignoring the sharper movement in mortgage-rate and credit proxies.",
        ],
        field_weights={"label": 0.4, "primary_proxy_family": 0.35, "falsifier": 0.25},
        paired_case_group="proxy_vs_pressure_homebuilder",
    ),
    make_case(
        case_id="v14cpi_002",
        track="finance_and_business_causal_reasoning",
        source_family=["XFinBench", "FinBen", "Finance Agent"],
        task_family="proxy_family_selection",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="analyst_memo",
        title="Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?",
        scenario="A crypto market packet compares majors, alt-token liquidity, on-chain activity, and exchange conditions after a sharp decline in a gaming token basket.",
        question="Which proxy family is the cleaner starting point for the selloff, and what would most directly falsify that interpretation?",
        truth_type="hybrid_structured_review",
        skills_required=["proxy_routing", "event_reasoning", "falsification"],
        slice_tags=["crypto", "proxy_routing", "liquidity", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Crypto desk note",
                "BTC and ETH were nearly flat on the day, but gaming and lower-liquidity alt tokens sold off hard. No exploit, governance failure, or delisting notice was reported for the focal token.",
            ),
            material(
                "table",
                "Cross-market snapshot",
                "BTC return: +0.3%. ETH return: +0.1%. Alt-token order-book depth: -35%. Perp funding on small tokens: sharply negative. Exchange maintenance on one retail-heavy venue: 2 hours. Game DAU: flat. On-chain fees for the project: flat.",
            ),
        ],
        options=[
            option("A", "Base-asset adoption is the cleaner proxy family."),
            option("B", "Retail liquidity and alt-beta risk appetite are the cleaner proxy family."),
            option("C", "A project-specific protocol exploit is the cleaner proxy family."),
            option("D", "Institutional ETF flows are the cleaner proxy family."),
        ],
        response_fields=["label", "primary_proxy_family", "falsifier"],
        canonical_answer={
            "label": "B",
            "primary_proxy_family": "retail_liquidity_and_alt_beta",
            "falsifier": "project_specific_activity_breaks_while_broad_alt_liquidity_normalizes",
        },
        evidence_summary=[
            "Majors were stable while lower-liquidity books and alt funding deteriorated sharply.",
            "Project-specific usage stayed flat, which argues against a token-specific adoption collapse.",
        ],
        common_failure_modes=[
            "Projecting a broad BTC/ETH narrative onto a move that is concentrated in low-liquidity alt exposure.",
            "Assuming a hack or exploit without any evidence packet support.",
        ],
        field_weights={"label": 0.4, "primary_proxy_family": 0.35, "falsifier": 0.25},
    ),
    make_case(
        case_id="v14cpi_003",
        track="finance_and_business_causal_reasoning",
        source_family=["BizBench", "XFinBench", "FinBen"],
        task_family="proxy_family_selection",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="analyst_memo",
        title="Airline Selloff: Fuel Shock Or Demand Crack?",
        scenario="An airline equity drawdown arrives alongside a commodity move, while booking and traffic indicators are updated in the same note.",
        question="Which proxy family should be treated as the primary causal read, and what would most clearly falsify it?",
        truth_type="hybrid_structured_review",
        skills_required=["proxy_routing", "domain_knowledge", "falsification"],
        slice_tags=["finance", "input_costs", "proxy_routing", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Airline sector note",
                "The stock fell after a sharp move in energy markets. Management did not cut capacity or demand commentary, and no labor disruption was disclosed.",
            ),
            material(
                "table",
                "Operating and market snapshot",
                "Jet fuel crack spread: +18%. Front-month crude: +11%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue guidance: flat. Wage agreement updates: none. FX basket: flat.",
            ),
        ],
        options=[
            option("A", "Fuel and input-cost pressure are the primary proxy family."),
            option("B", "End-demand weakness is the primary proxy family."),
            option("C", "Labor disruption is the primary proxy family."),
            option("D", "FX translation is the primary proxy family."),
        ],
        response_fields=["label", "primary_proxy_family", "falsifier"],
        canonical_answer={
            "label": "A",
            "primary_proxy_family": "fuel_and_input_cost_pressure",
            "falsifier": "forward_bookings_or_unit_revenue_break_while_fuel_pressure_eases",
        },
        evidence_summary=[
            "The sharpest moving variables are fuel-linked while bookings and unit-revenue guidance are stable.",
            "There is no evidence packet support for labor or FX being the dominant marginal driver.",
        ],
        common_failure_modes=[
            "Assuming all airline weakness is demand-driven without checking booking and unit-revenue evidence.",
            "Overweighting crude headlines without relating them to the actual airline cost channel.",
        ],
        field_weights={"label": 0.4, "primary_proxy_family": 0.35, "falsifier": 0.25},
        paired_case_group="proxy_vs_pressure_airline",
    ),
    make_case(
        case_id="v14cpi_004",
        track="finance_and_business_causal_reasoning",
        source_family=["XFinBench", "FinBen", "Finance Agent"],
        task_family="proxy_family_selection",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="analyst_memo",
        title="Small-Cap Software De-Rate: Duration Pressure Or Product Trouble?",
        scenario="A software stock sells off with a broader factor move while company-specific operating metrics are also reported.",
        question="Which proxy family is the cleaner explanation for the move, and what would most directly falsify that read?",
        truth_type="hybrid_structured_review",
        skills_required=["proxy_routing", "event_reasoning", "falsification"],
        slice_tags=["finance", "credit", "duration", "proxy_routing"],
        inputs=[
            material(
                "document_excerpt",
                "Software note",
                "The company reiterated annual ARR guidance and disclosed no outage, product recall, or major customer loss. The stock fell alongside a broader selloff in long-duration software names.",
            ),
            material(
                "table",
                "Factor and operating snapshot",
                "High-yield OAS: +75 bps. 10Y real yield: +19 bps. Small-cap software basket: -11%. ARR guidance: unchanged. Net revenue retention: 112% -> 111%. Churn: flat. Major incident count: 0.",
            ),
        ],
        options=[
            option("A", "Financing conditions and discount-rate duration are the cleaner proxy family."),
            option("B", "Product trouble is the cleaner proxy family."),
            option("C", "Channel inventory correction is the cleaner proxy family."),
            option("D", "Accounting restatement risk is the cleaner proxy family."),
        ],
        response_fields=["label", "primary_proxy_family", "falsifier"],
        canonical_answer={
            "label": "A",
            "primary_proxy_family": "financing_conditions_and_duration_pressure",
            "falsifier": "renewal_or_churn_metrics_break_even_if_credit_and_rate_proxies_stabilize",
        },
        evidence_summary=[
            "Macro duration and credit-sensitive software factors moved sharply while company operating metrics were largely intact.",
            "The packet does not contain company-specific failure evidence strong enough to outrank the factor move.",
        ],
        common_failure_modes=[
            "Inventing product trouble from price action alone.",
            "Ignoring the explicit sector-factor de-rating in the evidence packet.",
        ],
        field_weights={"label": 0.4, "primary_proxy_family": 0.35, "falsifier": 0.25},
    ),
    make_case(
        case_id="v14cpi_005",
        track="finance_and_business_causal_reasoning",
        source_family=["BizBench", "XFinBench", "CausalFlip"],
        task_family="bridge_noise_rejection",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="analyst_memo",
        title="Soybean Rally And Snack-Maker Weakness",
        scenario="A consumer staples note lists several moving commodities, but only some sit on the company’s true cost path.",
        question="Which candidate driver is most likely bridge noise rather than the core transmission channel?",
        truth_type="hybrid_structured_review",
        skills_required=["graph_reasoning", "domain_knowledge", "abduction"],
        slice_tags=["finance", "bridge_noise", "input_costs", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Staples note",
                "The stock traded lower after a basket of agricultural commodities moved higher. Management commentary emphasizes freight, packaging resin, palm oil, and cocoa as the main variable costs.",
            ),
            material(
                "table",
                "Cost exposure snapshot",
                "Soybeans: +9%. Palm oil: +4%. Cocoa: +6%. Packaging resin: +7%. Freight surcharge impact: +110 bps to COGS. Soy exposure in the focal brand mix: not material.",
            ),
        ],
        options=[
            option("A", "The soybean rally is most likely bridge noise rather than the core driver."),
            option("B", "Freight surcharges are most likely bridge noise rather than the core driver."),
            option("C", "Packaging-resin inflation is most likely bridge noise rather than the core driver."),
            option("D", "Palm-oil and cocoa costs are most likely bridge noise rather than the core driver."),
        ],
        response_fields=["label", "bridge_noise", "rationale_tag"],
        canonical_answer={
            "label": "A",
            "bridge_noise": "soybean_rally",
            "rationale_tag": "company_cost_structure_does_not_run_through_soybeans",
        },
        evidence_summary=[
            "The note explicitly says soy is not a material input for the focal brand mix.",
            "Freight, resin, palm oil, and cocoa all sit more directly on the company cost path.",
        ],
        common_failure_modes=[
            "Equating any agricultural headline with causal relevance to a food stock.",
            "Picking the most visible market move instead of the cleanest company-specific transmission channel.",
        ],
        field_weights={"label": 0.45, "bridge_noise": 0.35, "rationale_tag": 0.20},
    ),
    make_case(
        case_id="v14cpi_006",
        track="graph_and_mechanism",
        source_family=["CausalGraph2LLM", "CausalBench", "XFinBench"],
        task_family="transmission_supportability",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="analyst_memo",
        title="Regional Bank Stress And A Small-Cap SaaS Selloff",
        scenario="A software stock trades off during regional-bank stress even though the company has no direct deposit or lending disclosure in the packet.",
        question="Which transmission path is the most supportable causal explanation?",
        truth_type="hybrid_structured_review",
        skills_required=["graph_reasoning", "proxy_routing", "supportability"],
        slice_tags=["finance", "transmission", "supportability", "credit"],
        inputs=[
            material(
                "document_excerpt",
                "Market note",
                "The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.",
            ),
            material(
                "table",
                "Factor snapshot",
                "Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.",
            ),
        ],
        options=[
            option("A", "No plausible path exists from regional-bank stress to the software stock."),
            option("B", "Direct deposit-loss exposure is the most supportable path."),
            option("C", "A valuation-duration and refinancing channel is the most supportable path."),
            option("D", "A hardware inventory channel is the most supportable path."),
        ],
        response_fields=["label", "mechanism", "supportability"],
        canonical_answer={
            "label": "C",
            "mechanism": "valuation_duration_and_refinancing_channel",
            "supportability": "supported_but_indirect",
        },
        evidence_summary=[
            "The packet rules out direct deposit exposure, but a broader risk and financing channel remains plausible.",
            "High-yield spreads widened and duration-sensitive software names sold off together.",
        ],
        common_failure_modes=[
            "Assuming no path simply because the company lacks direct bank exposure.",
            "Inventing a balance-sheet crisis despite the explicit net-cash note.",
        ],
        field_weights={"label": 0.4, "mechanism": 0.35, "supportability": 0.25},
    ),
    make_case(
        case_id="v14cpi_007",
        track="graph_and_mechanism",
        source_family=["CausalGraph2LLM", "CausalFlip", "FinBen"],
        task_family="transmission_strength_judgment",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="mixed_modal_finance_qa",
        title="Rare-Earth Spike Into EV Gross Margin",
        scenario="A commodity shock looks intuitively relevant, but the evidence packet includes cost-share and contracting details that constrain near-term transmission.",
        question="How strong is the near-term transmission from rare-earth prices to the EV maker’s gross margin?",
        truth_type="hybrid_structured_review",
        skills_required=["graph_reasoning", "supportability", "domain_knowledge"],
        slice_tags=["finance", "transmission", "input_costs", "bridge_noise"],
        inputs=[
            material(
                "document_excerpt",
                "Supply-chain note",
                "Rare-earth spot prices jumped after export restrictions. The automaker’s procurement note says the focal materials are covered by fixed contracts for the next two quarters.",
            ),
            material(
                "table",
                "Cost-structure snapshot",
                "Rare-earth component share of COGS: 1.2%. Fixed-price coverage horizon: 2 quarters. Battery metals and logistics remain the larger variable exposures.",
            ),
        ],
        options=[
            option("A", "It is a strong and immediate primary driver of gross margin."),
            option("B", "It is a moderate near-term driver, but not the dominant one."),
            option("C", "It is a weak, bridge-heavy near-term channel rather than a clean primary driver."),
            option("D", "No judgment of any kind is possible from the packet."),
        ],
        response_fields=["label", "transmission_strength", "blocking_factor"],
        canonical_answer={
            "label": "C",
            "transmission_strength": "weak_near_term",
            "blocking_factor": "fixed_contracts_and_low_cost_share",
        },
        evidence_summary=[
            "The cost share is small and the contract coverage delays pass-through.",
            "The packet explicitly points to larger variable exposures elsewhere in the cost stack.",
        ],
        common_failure_modes=[
            "Overweighting the most dramatic commodity headline without checking cost share and contract timing.",
            "Calling the move impossible to assess despite clear packet constraints.",
        ],
        field_weights={"label": 0.4, "transmission_strength": 0.3, "blocking_factor": 0.3},
    ),
    make_case(
        case_id="v14cpi_008",
        track="natural_event_causality",
        source_family=["CRAB", "ExpliCa", "Finance Agent"],
        task_family="primary_driver_vs_amplifier",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="news_narrative",
        title="Biotech Rally: Primary Driver Or Pure Squeeze?",
        scenario="A market-news packet contains a regulatory catalyst, a later rumor, and evidence that short interest may have amplified the move.",
        question="Which explanation best fits the move without overstating the evidence?",
        truth_type="expert_labeled",
        skills_required=["event_reasoning", "temporal_vs_causal", "abduction"],
        slice_tags=["event_analysis", "causal_vs_temporal", "amplification", "finance"],
        inputs=[
            material(
                "news_packet",
                "Event timeline",
                "09:00: FDA advisory panel votes favorably on the therapy. 09:05: stock opens sharply higher. 12:10: an unconfirmed social-media rumor mentions a possible acquisition. Short interest entering the day was 24% of float.",
            ),
            material(
                "table",
                "Intraday move summary",
                "Open-to-10am move: +21%. Noon-to-close incremental move: +6%. Borrow fee: elevated. Company filings: no acquisition filing or comment.",
            ),
        ],
        options=[
            option("A", "The unconfirmed acquisition rumor is the primary driver."),
            option("B", "Short-squeeze dynamics are the primary driver, with no stronger causal event in the packet."),
            option("C", "The FDA advisory-panel vote is the primary driver, while squeeze dynamics likely amplified the move."),
            option("D", "No supportable causal read is possible from the packet."),
        ],
        response_fields=["label", "primary_driver", "amplifier"],
        canonical_answer={
            "label": "C",
            "primary_driver": "fda_advisory_panel_vote",
            "amplifier": "short_squeeze_dynamics",
        },
        evidence_summary=[
            "Most of the move occurred immediately after the regulatory event and before the rumor appeared.",
            "Short interest can explain amplification without replacing the primary catalyst.",
        ],
        common_failure_modes=[
            "Treating the later rumor as primary despite the timing mismatch.",
            "Collapsing primary driver and amplifier into the same answer.",
        ],
        field_weights={"label": 0.4, "primary_driver": 0.35, "amplifier": 0.25},
    ),
    make_case(
        case_id="v14cpi_009",
        track="industrial_intervention_and_estimation",
        source_family=["InterveneBench", "CausalReasoningBenchmark", "BizBench"],
        task_family="bundled_intervention_supportability",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="study_design_prompt",
        title="Price Cut And Sales-Comp Rewrite In The Same Week",
        scenario="Leadership wants the effect of a price cut on unit sales, but the operating packet shows another major commercial intervention at the same time and in the same weak regions.",
        question="Is the causal effect of the price cut on units identified from the observed packet?",
        truth_type="expert_labeled",
        skills_required=["identification", "supportability", "abstention"],
        slice_tags=["intervention", "identification", "bundled_treatment", "business"],
        inputs=[
            material(
                "document_excerpt",
                "Commercial rollout note",
                "The company reduced list price by 8% in the weakest four regions and simultaneously changed sales compensation to reward unit volume instead of gross profit dollars.",
            ),
            material(
                "table",
                "Observed outcome summary",
                "The treated regions saw unit growth accelerate after the rollout. Untreated regions kept the old price and old comp plan. No randomization or staggered timing was used.",
            ),
        ],
        options=[
            option("A", "Yes. A simple before/after comparison identifies the price effect."),
            option("B", "Yes. Region controls are enough to identify the price effect."),
            option("C", "No. The packet bundles two interventions on selected weak regions."),
            option("D", "Yes. A treated-vs-untreated snapshot identifies the price effect."),
        ],
        response_fields=["label", "identified", "blocking_issue"],
        canonical_answer={
            "label": "C",
            "identified": False,
            "blocking_issue": "bundled_intervention_and_targeted_rollout",
        },
        evidence_summary=[
            "Price and comp changed together on the same weak regions, so the packet does not isolate price alone.",
            "There is no randomization or staggered variation to separate the two levers cleanly.",
        ],
        common_failure_modes=[
            "Treating any untreated region as a valid control despite targeted rollout.",
            "Ignoring the incentive-plan rewrite because the price cut feels more salient.",
        ],
        field_weights={"label": 0.45, "identified": 0.30, "blocking_issue": 0.25},
    ),
    make_case(
        case_id="v14cpi_010",
        track="industrial_intervention_and_estimation",
        source_family=["InterveneBench", "CausalReasoningBenchmark", "causalAssembly"],
        task_family="targeted_rollout_design_choice",
        generation_pipeline="domain_knowledge_plus_news_to_structural_task",
        prompt_style="study_design_prompt",
        title="Predictive Maintenance Rolled Out To The Worst Plants First",
        scenario="A maintenance model was adopted first where failures were already highest, and leadership wants a credible evaluation design.",
        question="Which design is most defensible for estimating the model’s effect, and what is the main threat to validity?",
        truth_type="expert_labeled",
        skills_required=["identification", "study_design", "abstention"],
        slice_tags=["intervention", "targeted_rollout", "regression_to_mean", "industrial_process"],
        inputs=[
            material(
                "operational_log",
                "Rollout summary",
                "The predictive-maintenance model was launched first at plants with the highest prior failure rates. Failure rates fell after deployment, but the untreated plants were lower-risk to begin with.",
            ),
            material(
                "table",
                "Plant summary",
                "Four treated plants adopted in month 1, four control plants remained on the old process. Treated plants started with materially worse pre-period failure levels.",
            ),
        ],
        options=[
            option("A", "A simple before/after comparison is the most defensible design."),
            option("B", "A matched or staggered difference-in-differences event study with pretrend checks is the most defensible design."),
            option("C", "A post-only treated-vs-control cross-section is the most defensible design."),
            option("D", "Instrumenting treatment with plant size is the most defensible design."),
        ],
        response_fields=["label", "design", "main_threat"],
        canonical_answer={
            "label": "B",
            "design": "matched_or_staggered_difference_in_differences_event_study",
            "main_threat": "targeted_rollout_and_regression_to_mean",
        },
        evidence_summary=[
            "The rollout is non-random and correlated with pre-period failure levels.",
            "A DID/event-study framing is the cleanest public-dev answer because it explicitly tests pretrends and uses staggered structure when available.",
        ],
        common_failure_modes=[
            "Choosing before/after because failures visibly fell.",
            "Ignoring regression to the mean in a targeted rollout.",
        ],
        field_weights={"label": 0.4, "design": 0.35, "main_threat": 0.25},
    ),
    make_case(
        case_id="v14cpi_011",
        track="industrial_intervention_and_estimation",
        source_family=["CausalReasoningBenchmark", "BizBench", "RealCause"],
        task_family="selection_bias_supportability",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="study_design_prompt",
        title="Credit-Limit Increases For Prequalified Users",
        scenario="A consumer-finance team increased credit limits only for users already scored as especially attractive, then asked for the treatment effect on purchase frequency.",
        question="Can the treated-vs-untreated mean difference identify the effect on purchase frequency?",
        truth_type="expert_labeled",
        skills_required=["identification", "supportability", "abstention"],
        slice_tags=["intervention", "selection_bias", "business", "identification"],
        inputs=[
            material(
                "document_excerpt",
                "Risk-team note",
                "Only prequalified users with high internal scores received the limit increase. The untreated pool contains more low-score and lower-spend customers.",
            ),
            material(
                "table",
                "Outcome summary",
                "Treated users increased purchase frequency after the offer. Current observables include age bucket, region, and merchant mix, but not latent spending appetite or the full internal scorecard.",
            ),
        ],
        options=[
            option("A", "Yes. The treated-vs-untreated mean difference identifies the treatment effect."),
            option("B", "Yes. The current covariates are enough to remove the bias."),
            option("C", "No. Selection on latent spending propensity still blocks identification."),
            option("D", "Yes. Stable merchant mix is sufficient to identify the effect."),
        ],
        response_fields=["label", "identified", "blocking_issue"],
        canonical_answer={
            "label": "C",
            "identified": False,
            "blocking_issue": "selection_on_latent_purchase_propensity",
        },
        evidence_summary=[
            "Treatment assignment depends on an internal score that the analyst does not fully observe.",
            "The untreated pool differs on the same latent propensity that likely affects future purchases.",
        ],
        common_failure_modes=[
            "Assuming any observed covariates guarantee ignorability.",
            "Treating stable merchant mix as a substitute for assignment information.",
        ],
        field_weights={"label": 0.45, "identified": 0.30, "blocking_issue": 0.25},
    ),
    make_case(
        case_id="v14cpi_012",
        track="industrial_intervention_and_estimation",
        source_family=["InterveneBench", "CausalReasoningBenchmark", "causalAssembly"],
        task_family="simultaneous_operations_change",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="study_design_prompt",
        title="Warehouse Expedite Policy And Temporary Staffing",
        scenario="An operations packet shows late shipments falling after a new expedite policy, but staffing changed in the same window.",
        question="Is the expedite-policy effect identified from the observed packet, and what is the most important confound?",
        truth_type="expert_labeled",
        skills_required=["identification", "supportability", "abstention"],
        slice_tags=["intervention", "operations", "confounder", "industrial_process"],
        inputs=[
            material(
                "operational_log",
                "Operations note",
                "A warehouse introduced a new expedite policy during peak season. The same week, temporary staffing was increased by 18% and overtime rules were relaxed.",
            ),
            material(
                "table",
                "Late-shipment summary",
                "Late shipments fell from 9.4% to 6.7% after the policy week. No site-level stagger or holdout group is available in the packet.",
            ),
        ],
        options=[
            option("A", "Yes. Staffing is too small to matter here."),
            option("B", "Yes. Controlling for shift is enough to identify the policy effect."),
            option("C", "No. The simultaneous temporary-staffing change is the key confound."),
            option("D", "No. The outcome metric itself is unusable."),
        ],
        response_fields=["label", "identified", "blocking_issue"],
        canonical_answer={
            "label": "C",
            "identified": False,
            "blocking_issue": "simultaneous_temporary_staffing_change",
        },
        evidence_summary=[
            "The packet changes operational capacity and expedite rules together in the same window.",
            "Without staggered adoption or a holdout, attribution to expedite policy alone is not supportable.",
        ],
        common_failure_modes=[
            "Treating the bigger named intervention as the only causal lever.",
            "Assuming a good outcome metric implies clean identification.",
        ],
        field_weights={"label": 0.45, "identified": 0.30, "blocking_issue": 0.25},
    ),
    make_case(
        case_id="v14cpi_013",
        track="agentic_live_analysis",
        source_family=["Finance Agent", "XFinBench", "CausalReasoningBenchmark"],
        task_family="pressure_test_design",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="agent_brief",
        title="Which First Pressure Test Separates Financing Stress From Demand Softness?",
        scenario="A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.",
        question="Which first pressure test would best separate financing stress from demand softness?",
        truth_type="hybrid_structured_review",
        skills_required=["pressure_test_design", "proxy_routing", "decision_theory"],
        slice_tags=["pressure_test", "finance", "proxy_routing", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Agent brief",
                "Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.",
            ),
            material(
                "table",
                "Commercial snapshot",
                "New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.",
            ),
        ],
        options=[
            option("A", "Stress commodity input costs and inspect gross margin."),
            option("B", "Stress financing conditions and inspect orders plus cancellations."),
            option("C", "Stress FX and inspect backlog conversion."),
            option("D", "Stress labor availability and inspect headcount growth."),
        ],
        response_fields=["label", "stress_target", "readout"],
        canonical_answer={
            "label": "B",
            "stress_target": "financing_conditions",
            "readout": "order_intake_and_cancellations",
        },
        evidence_summary=[
            "The open causal split is financing friction versus true demand softness.",
            "Orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions.",
        ],
        common_failure_modes=[
            "Choosing a lever unrelated to the live uncertainty.",
            "Looking at margin before testing the order-flow channel that actually separates the stories.",
        ],
        field_weights={"label": 0.4, "stress_target": 0.35, "readout": 0.25},
        paired_case_group="proxy_vs_pressure_homebuilder",
    ),
    make_case(
        case_id="v14cpi_014",
        track="agentic_live_analysis",
        source_family=["Finance Agent", "BizBench", "XFinBench"],
        task_family="pressure_test_design",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="agent_brief",
        title="Fuel Shock Or Demand Weakness: Which Probe Comes First?",
        scenario="An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.",
        question="Which first pressure test most cleanly distinguishes fuel shock from demand weakness?",
        truth_type="hybrid_structured_review",
        skills_required=["pressure_test_design", "domain_knowledge", "decision_theory"],
        slice_tags=["pressure_test", "finance", "input_costs", "airline"],
        inputs=[
            material(
                "document_excerpt",
                "Agent brief",
                "The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.",
            ),
            material(
                "table",
                "Sector snapshot",
                "Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.",
            ),
        ],
        options=[
            option("A", "Stress jet-fuel costs and inspect unit margin or EPS sensitivity."),
            option("B", "Stress load factor and inspect fuel hedges."),
            option("C", "Stress FX and inspect baggage-fee revenue."),
            option("D", "Stress wage inflation and inspect loyalty signups."),
        ],
        response_fields=["label", "stress_target", "readout"],
        canonical_answer={
            "label": "A",
            "stress_target": "jet_fuel_costs",
            "readout": "unit_margin_or_eps_sensitivity",
        },
        evidence_summary=[
            "The packet already shows stable demand-side evidence and a large energy move.",
            "Margin and EPS sensitivity are the most direct downstream readouts of a fuel-cost stress.",
        ],
        common_failure_modes=[
            "Choosing a demand-side probe despite the packet already showing stable booking evidence.",
            "Picking a variable that is not downstream of the suspected cost channel.",
        ],
        field_weights={"label": 0.4, "stress_target": 0.35, "readout": 0.25},
        paired_case_group="proxy_vs_pressure_airline",
    ),
    make_case(
        case_id="v14cpi_015",
        track="agentic_live_analysis",
        source_family=["Finance Agent", "XFinBench", "CausalReasoningBenchmark"],
        task_family="pressure_test_design",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="agent_brief",
        title="EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?",
        scenario="A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.",
        question="Which first pressure test best distinguishes lithium pass-through from customer inventory reset?",
        truth_type="hybrid_structured_review",
        skills_required=["pressure_test_design", "proxy_routing", "decision_theory"],
        slice_tags=["pressure_test", "finance", "inventory", "input_costs"],
        inputs=[
            material(
                "document_excerpt",
                "Agent brief",
                "Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.",
            ),
            material(
                "table",
                "Supplier snapshot",
                "Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.",
            ),
        ],
        options=[
            option("A", "Stress lithium prices and inspect next-quarter gross margin."),
            option("B", "Stress customer inventory and build schedules, then inspect shipments and backlog conversion."),
            option("C", "Stress FX and inspect operating expenses."),
            option("D", "Stress energy prices and inspect depreciation."),
        ],
        response_fields=["label", "stress_target", "readout"],
        canonical_answer={
            "label": "B",
            "stress_target": "customer_inventory_reset",
            "readout": "shipments_and_backlog_conversion",
        },
        evidence_summary=[
            "Customer inventory and build schedules are the variables most directly tied to the supplier’s shipment softness in the packet.",
            "Lithium softness alone does not explain a slower backlog conversion nearly as cleanly.",
        ],
        common_failure_modes=[
            "Defaulting to the flashier commodity move instead of the more direct downstream transmission path.",
            "Reading margin before checking the shipment path that actually distinguishes the stories.",
        ],
        field_weights={"label": 0.4, "stress_target": 0.35, "readout": 0.25},
    ),
    make_case(
        case_id="v14cpi_016",
        track="agentic_live_analysis",
        source_family=["Finance Agent", "BizBench", "CausalReasoningBenchmark"],
        task_family="pressure_test_design",
        generation_pipeline="simple_qa_to_complex_analysis",
        prompt_style="agent_brief",
        title="Residential Solar Miss: Policy Step-Down Or Sales Execution?",
        scenario="The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.",
        question="Which pressure test most directly challenges the thesis that policy incentive step-down is the main driver?",
        truth_type="hybrid_structured_review",
        skills_required=["pressure_test_design", "event_reasoning", "falsification"],
        slice_tags=["pressure_test", "policy", "finance", "falsification"],
        inputs=[
            material(
                "document_excerpt",
                "Agent brief",
                "Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.",
            ),
            material(
                "table",
                "Sales funnel snapshot",
                "Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.",
            ),
        ],
        options=[
            option("A", "Stress incentive-policy generosity and inspect lead-to-booking conversion."),
            option("B", "Stress panel input costs and inspect gross margin."),
            option("C", "Stress installer hiring and inspect warehouse rent."),
            option("D", "Stress bitcoin and inspect lead generation."),
        ],
        response_fields=["label", "stress_target", "readout"],
        canonical_answer={
            "label": "A",
            "stress_target": "incentive_policy_generosity",
            "readout": "lead_to_booking_conversion",
        },
        evidence_summary=[
            "The leading thesis is specifically about incentive generosity, so the cleanest challenge is to stress that lever and inspect the conversion step most directly tied to purchase economics.",
            "Lead volume moved far less than conversion, which makes the conversion readout more decision-relevant than top-of-funnel traffic.",
        ],
        common_failure_modes=[
            "Choosing a lever that is unrelated to the stated uncertainty.",
            "Looking at margin instead of the funnel step most exposed to incentive economics.",
        ],
        field_weights={"label": 0.4, "stress_target": 0.35, "readout": 0.25},
    ),
]


def build_cases() -> dict:
    cases = [entry["case"] for entry in PACK_CASES]
    return {
        "version": "v14-alpha-causal-proxy-intervention-cases",
        "split": "public_dev",
        "description": (
            "Focused public-dev pack designed to be harder on proxy routing, "
            "bridge-noise rejection, intervention boundaries, and pressure-test design "
            "than the main 21-case v14 pack."
        ),
        "case_count": len(cases),
        "notes": [
            "Ground truth is separated into causal_proxy_intervention_ground_truth.json.",
            "These cases are intentionally shaped to better expose skill advantages on causal/proxy/intervention tasks.",
        ],
        "cases": cases,
    }


def build_ground_truth() -> dict:
    cases = [entry["ground_truth"] for entry in PACK_CASES]
    return {
        "version": "v14-alpha-causal-proxy-intervention-ground-truth",
        "split": "public_dev",
        "case_count": len(cases),
        "notes": [
            "This answer key is for the focused causal/proxy/intervention pack, not the main 21-case v14 pack.",
            "Scoring should use per-case field weights and not a single exact-match scalar only.",
        ],
        "cases": cases,
    }


def build_markdown(cases: dict, ground_truth: dict) -> str:
    ground_truth_by_id = {case["id"]: case for case in ground_truth["cases"]}
    lines = [
        "# v14 Causal / Proxy / Intervention Focus Pack",
        "",
        "This focused pack adds harder public-dev cases for the benchmark slices where we expect stronger separation on causal reasoning, proxy routing, bridge-noise rejection, intervention supportability, and pressure-test design.",
        "",
        f"- Case count: `{cases['case_count']}`",
        "- Split: `public_dev`",
        "- Files: `causal_proxy_intervention_cases.json`, `causal_proxy_intervention_ground_truth.json`",
        "",
    ]

    for case in cases["cases"]:
        gt = ground_truth_by_id[case["id"]]
        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Track: `{case['track']}`",
                f"- Task family: `{case['task_family']}`",
                f"- Prompt style: `{case['prompt_style']}`",
                f"- Truth type: `{case['truth_type']}`",
                "",
                "**Scenario**",
                "",
                case["scenario"],
                "",
                "**Question**",
                "",
                case["question"],
                "",
                "**Materials**",
                "",
            ]
        )
        for item in case["instantiated_inputs"]:
            lines.extend(
                [
                    f"- `{item['type']}` — **{item['title']}**",
                    "",
                    item["content"],
                    "",
                ]
            )
        lines.append("**Options**")
        lines.append("")
        for item in case["options"]:
            lines.append(f"- `{item['label']}`: {item['text']}")
        lines.extend(
            [
                "",
                "**Ground truth**",
                "",
                "```json",
                json.dumps(gt["canonical_answer"], indent=2, ensure_ascii=True),
                "```",
                "",
                "**Evidence summary**",
                "",
            ]
        )
        for item in gt["evidence_summary"]:
            lines.append(f"- {item}")
        lines.extend(
            [
                "",
                "**Common failure modes**",
                "",
            ]
        )
        for item in gt["common_failure_modes"]:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    cases = build_cases()
    ground_truth = build_ground_truth()
    CASES_PATH.write_text(json.dumps(cases, indent=2, ensure_ascii=True) + "\n")
    GROUND_TRUTH_PATH.write_text(json.dumps(ground_truth, indent=2, ensure_ascii=True) + "\n")
    MARKDOWN_PATH.write_text(build_markdown(cases, ground_truth))
    print(f"Wrote {CASES_PATH}")
    print(f"Wrote {GROUND_TRUTH_PATH}")
    print(f"Wrote {MARKDOWN_PATH}")


if __name__ == "__main__":
    main()
