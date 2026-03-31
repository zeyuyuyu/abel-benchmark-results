# v14 Track H Causal Ops Cases

This pack evaluates practical causal-network operations in analyst language.
Ground truth is generated from a frozen CAP snapshot and stored separately.

- Case count: `24`
- Track: `causal_network_operations`
- Evaluation regime: `frozen_evidence_public_dev`

## v14h_001 — Cross-Asset Upside Pick (NVDA/TSLA/GS/AVGO)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. NVDA
- B. TSLA
- C. GS
- D. AVGO

Ground truth:
- \boxed{D}

## v14h_002 — Cross-Asset Upside Pick (ETHUSD/XOM/AVGO/AMZN)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. ETHUSD
- B. XOM
- C. AVGO
- D. AMZN

Ground truth:
- \boxed{A}

## v14h_003 — Cross-Asset Upside Pick (AMZN/ADAUSD/GS/AVGO)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. AMZN
- B. ADAUSD
- C. GS
- D. AVGO

Ground truth:
- \boxed{D}

## v14h_004 — Cross-Asset Upside Pick (NVDA/AMZN/INTC/AAPL)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. NVDA
- B. AMZN
- C. INTC
- D. AAPL

Ground truth:
- \boxed{C}

## v14h_005 — Cross-Asset Upside Pick (JPM/AMZN/PYPL/AAPL)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. JPM
- B. AMZN
- C. PYPL
- D. AAPL

Ground truth:
- \boxed{B}

## v14h_006 — Cross-Asset Upside Pick (JPM/META/GS/AMZN)

- Task family: `cross_asset_upside_selection`
- Category: `upside_selection`
Question:
You are preparing a one-step tactical note from an internal causal market network. Among the following assets, which one currently has the strongest upside signal?

Options:
- A. JPM
- B. META
- C. GS
- D. AMZN

Ground truth:
- \boxed{B}

## v14h_007 — Direct Upstream Driver For XOM

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on XOM, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. AAPL
- B. ADAUSD
- C. INTC
- D. ECCX

Ground truth:
- \boxed{D}

## v14h_008 — Direct Upstream Driver For XRPUSD

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on XRPUSD, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. GS
- B. GOOGL
- C. AIV
- D. COIN

Ground truth:
- \boxed{C}

## v14h_009 — Direct Upstream Driver For ETHUSD

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on ETHUSD, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. NVDA
- B. XRPUSD
- C. SSTK
- D. DOGEUSD

Ground truth:
- \boxed{C}

## v14h_010 — Direct Upstream Driver For META

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on META, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. CVX
- B. GOOGL
- C. AVGO
- D. PSFE

Ground truth:
- \boxed{D}

## v14h_011 — Direct Upstream Driver For CVX

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on CVX, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. NVDA
- B. GS
- C. INTC
- D. BML-PG

Ground truth:
- \boxed{D}

## v14h_012 — Direct Upstream Driver For AAPL

- Task family: `direct_parent_identification`
- Category: `parent_identification`
Question:
For risk decomposition on AAPL, which candidate is currently a direct upstream driver in the causal market network?

Options:
- A. NVDA
- B. AMZN
- C. PRIMEUSD
- D. XOM

Ground truth:
- \boxed{C}

## v14h_013 — Role Of ECCX Relative To XOM

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of ECCX relative to XOM?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{A}

## v14h_014 — Role Of IMOUSD Relative To COIN

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of IMOUSD relative to COIN?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{A}

## v14h_015 — Role Of DANAUSD Relative To DAL

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of DANAUSD relative to DAL?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{A}

## v14h_016 — Role Of AEROUSD Relative To GOOGL

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of AEROUSD relative to GOOGL?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{B}

## v14h_017 — Role Of AIV Relative To XRPUSD

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of AIV relative to XRPUSD?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{A}

## v14h_018 — Role Of AGNCM Relative To TSLA

- Task family: `markov_role_classification`
- Category: `markov_role`
Question:
In the current causal market network, what is the relationship role of AGNCM relative to TSLA?

Options:
- A. Parent (direct upstream driver)
- B. Child (direct downstream receiver)
- C. Spouse (shares a child but not a direct parent/child link)
- D. None of the above

Ground truth:
- \boxed{A}

## v14h_019 — Path Reachability: TDROPUSD -> GS

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from TDROPUSD reach GS in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{A}

## v14h_020 — Path Reachability: PYPL -> DOGEUSD

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from PYPL reach DOGEUSD in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{B}

## v14h_021 — Path Reachability: SFIUSD -> INTC

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from SFIUSD reach INTC in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{A}

## v14h_022 — Path Reachability: XRPUSD -> XOM

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from XRPUSD reach XOM in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{B}

## v14h_023 — Path Reachability: AIV -> XRPUSD

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from AIV reach XRPUSD in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{A}

## v14h_024 — Path Reachability: ADAUSD -> XRPUSD

- Task family: `directed_path_reachability`
- Category: `path_reachability`
Question:
For fast shock-propagation screening, can a directed causal influence from ADAUSD reach XRPUSD in the current market network?

Options:
- A. Yes, there is at least one directed causal path.
- B. No, no directed causal path is present.

Ground truth:
- \boxed{B}
