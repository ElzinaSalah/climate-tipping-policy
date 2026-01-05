# Climate Tipping Risk, Carbon Budgets, and Optimal Climate Policy

## Overview

This repository presents a quantitative research project analyzing **optimal climate policy under the risk of climate tipping points**. The project develops a dynamic stochastic model in which cumulative carbon emissions increase the probability of irreversible climate transitions, leading to permanent welfare losses.

The analysis combines **climate science**, **economic dynamics**, and **policy design**, and is implemented entirely in Python using transparent numerical methods. The project is structured as a sequence of teaching-quality notebooks, progressing from physical intuition to strategic interaction and policy instruments.

The primary goal of the project is to understand how **carbon budgets, strategic behavior, and policy coordination** affect tipping-point risk and long-run welfare.

---

## Key Research Questions

- How should climate policy be designed when tipping points are uncertain but potentially catastrophic?
- How does the presence of tipping risk alter optimal emissions and carbon removal pathways?
- How do non-cooperative national policies compare to coordinated global action?
- Can policy instruments such as carbon pricing, transfers, and climate clubs decentralize the socially optimal outcome?
- How do explicit carbon budget constraints shape optimal policy under deep uncertainty?

---

## Conceptual Framework

### Climate Dynamics

Atmospheric carbon evolves according to a stock equation:

\[
C_{t+1} = C_t + E_t - R_t
\]

where:
- \( C_t \) is atmospheric carbon stock (GtCO₂),
- \( E_t \) denotes emissions (GtCO₂/year),
- \( R_t \) denotes carbon removal (GtCO₂/year).

Cumulative carbon accumulation increases the probability of crossing an irreversible climate tipping point.

---

### Tipping Risk

Tipping events are modeled probabilistically using a **hazard function**:

\[
h(C_t) = \frac{1}{1 + \exp[-a(C_t - C^*)]}
\]

where:
- \( C^* \) is a critical carbon threshold,
- \( a \) governs the steepness of tipping risk.

If tipping occurs, the system enters a permanently damaged state with reduced welfare.

---

### Economic Objective

Social welfare is defined recursively using a dynamic programming framework:

\[
V(C_t) = \max_{E_t, R_t}
\left[
u(E_t, R_t)
+ \beta \left( (1 - h_t) V(C_{t+1}) + h_t V^{\text{post}} \right)
\right]
\]

where:
- \( u(\cdot) \) is instantaneous utility,
- \( \beta \) is the discount factor,
- \( V^{\text{post}} \) is welfare after tipping.

This formulation captures forward-looking policy under irreversible risk.

---

## Strategic Interaction

The project extends the model to multiple regions:

- Regions choose emissions and removals strategically.
- Tipping risk depends on **global** carbon accumulation.
- Non-cooperative Nash equilibria are compared to a cooperative social planner.

This highlights the free-rider problem inherent in climate policy under tipping risk.

---

## Policy Instruments

The analysis evaluates several policy mechanisms:

- **Carbon pricing** to internalize global tipping externalities
- **International transfers** to sustain cooperation
- **Climate clubs** and **border carbon adjustments** to enforce participation
- **Carbon budget constraints** reflecting physical climate limits

Each instrument is assessed for its ability to replicate the socially optimal outcome.

---

## Repository Structure

climate-tipping-policy/
│
├── notebooks/
│ ├── 01_introduction_and_physical_intuition.ipynb
│ ├── 02_tipping_risk_and_welfare.ipynb
│ ├── 03_carbon_removal_as_insurance.ipynb
│ ├── 04_optimal_policy_under_tipping.ipynb
│ ├── 05_carbon_budget_constraints.ipynb
│ ├── 06_heterogeneous_regions_and_strategic_behavior.ipynb
│ ├── 07_nash_equilibrium_and_global_cooperation.ipynb
│ ├── 08_carbon_pricing_and_transfers.ipynb
│ ├── 09_climate_clubs_and_border_adjustments.ipynb
│ └── 10_policy_summary_for_decision_makers.ipynb
│
├── requirements.txt
└── README.md



---

## Methodological Features

- Dynamic programming and value function iteration
- Explicit modeling of irreversibility and catastrophe risk
- Strategic interaction between heterogeneous regions
- Numerical efficiency and reproducibility
- Units clearly labeled throughout simulations and plots

---

## Policy Relevance

This project contributes to ongoing debates on:

- Carbon budgets and safe climate thresholds
- The economic value of early mitigation
- International coordination under asymmetric incentives
- Policy design under deep uncertainty and irreversibility

The framework is suitable for extension toward integrated assessment modeling, empirical calibration, and policy evaluation.

---

## Intended Audience

- PhD programs in environmental economics, climate policy, and sustainability
- Researchers in climate risk and integrated assessment modeling
- Policy analysts working on carbon budgets and international climate cooperation

---

## Status

This repository represents an independent research attempt. All results are illustrative and designed to emphasize transparency, intuition, and methodological clarity.

---

## Contact

**Elzina Salah**  
Climate & Environmental Economics  
GitHub: https://github.com/ElzinaSalah


