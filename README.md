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

---
## Refrences
Lenton, T. M., et al. (2008).
Tipping elements in the Earth’s climate system.
Proceedings of the National Academy of Sciences, 105(6), 1786–1793.

Lenton, T. M., et al. (2019).
Climate tipping points — too risky to bet against.
Nature, 575, 592–595.

Armstrong McKay, D. I., et al. (2022).
Exceeding 1.5°C global warming could trigger multiple climate tipping points.
Science, 377(6611).

Lemoine, D., & Traeger, C. (2014).
Watch your step: Optimal policy in a tipping climate.
American Economic Journal: Economic Policy, 6(1), 137–166.

Cai, Y., Judd, K. L., & Lontzek, T. S. (2016).
The social cost of carbon with economic and climate risks.
Journal of Political Economy, 124(5), 1445–1487.

Dietz, S., Rising, J., Stoerk, T., & Wagner, G. (2021).
Economic impacts of tipping points in the climate system.
Proceedings of the National Academy of Sciences, 118(34).

Archer, D. (2005).
Fate of fossil fuel CO₂ in geologic time.
Journal of Geophysical Research, 110(C9).

Joos, F., et al. (2013).
Carbon dioxide and climate impulse response functions for the computation of greenhouse gas metrics.
Atmospheric Chemistry and Physics, 13, 2793–2825.

Nordhaus, W. D. (2015).
Climate clubs: Overcoming free-riding in international climate policy.
American Economic Review, 105(4), 1339–1370.

Stern, N. (2007).
The Economics of Climate Change: The Stern Review.
Cambridge University Press.

---
## Repository Structure

``` 
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
``` 


