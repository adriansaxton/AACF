# AI adoption assessment: Westmere Standards Agency (fictional)

Assessed against AI Adoption Controls Framework version 1.0.1. Report generated from `westmere-assessment.xlsx`; results are recomputed from the levels and targets entered. This is a framework assessment, not a certification or legal compliance opinion.

| | |
|---|---|
| Sector | UK public sector: arm's-length body that sets and checks technical standards for a regulated industry |
| Size | About 2,000 staff; data team of six; Microsoft 365 Copilot licensed to 600 staff |
| Scope of assessment | Whole organisation. All AI in use or in development at November 2026: Microsoft 365 Copilot (agents and plugins switched off in the tenant), the correspondence triage classifier pilot (a model tuned by the data team, planned to go live in January 2027), the guidance library search assistant pilot, and AI features in bought products. Three uses in all, so every use was sampled. |
| Assessor | Self-assessment led by the Head of Data (J. Okafor); security controls assessed by the Head of Information Assurance (S. Lindqvist); challenge from the Head of Internal Audit (P. Rourke) |
| Assessment date | 2026-11-09 |
| Assessment sponsor | Chief Operating Officer (R. Pellow), executive sponsor for AI |
| Notes | Invented organisation for the AACF worked example. Any resemblance to a real body is coincidental. |

## Scope: overlays

| Overlay | Applies | Reason |
|---|---|---|
| PUB Public body | Yes | An arm's-length public body with public duties, in mandatory scope for algorithmic transparency records. |
| PRV Provides AI to others | No | All AI is for Westmere's own use; it offers no AI service, product or model to anyone else. |
| HIR Regulated or high-impact use | No | No use decides or shapes people's rights, safety or access to services: triage only suggests a team for each letter and a person checks every suggestion, and safety reports arrive through the separate statutory reporting line, not the correspondence mailbox. Revisit at the triage go-live review. |
| GEN Generative AI | Yes | Microsoft 365 Copilot for 600 staff, and the search assistant generates answers from the guidance library. |
| AGT Agentic AI | No | No AI acts in other systems: Copilot agents and plugins are switched off and the triage classifier only suggests a route. |
| BLD Builds or tunes its own models | Yes | The data team tuned the triage classifier on labelled letters and built the search assistant's retrieval pipeline. |

## Headline

**5 of 91 scored controls (5%) are at the Level 3 baseline.** 6 of 91 (7%) are at their agreed target.

Distribution of levels: Level 0: 4, Level 1: 23, Level 2: 59, Level 3: 4, Level 4: 1, Level 5: 0.

Not counted in those figures: 2 with insufficient evidence, 0 not assessed, 0 not applicable. Of 93 controls in all.

Mean level 1.7 (a descriptive average for trends only; the scale is ordered, not evenly spaced).

## By domain

| Domain | Scored | 0 | 1 | 2 | 3 | 4 | 5 | At baseline | At target | Insufficient or not assessed |
|---|---|---|---|---|---|---|---|---|---|---|
| STR Strategy & Value | 8 | 2 | 2 | 4 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 0 |
| GOV Governance & Accountability | 10 | 1 | 2 | 7 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 0 |
| RSK Risk, Ethics & Compliance | 9 | 0 | 3 | 6 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 0 |
| POR Portfolio & Use Cases | 9 | 0 | 2 | 7 | 0 | 0 | 0 | 0 (0%) | 1 (11%) | 0 |
| OPM Operating Model & Delivery | 9 | 0 | 4 | 5 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 1 |
| DAT Data & Information | 8 | 0 | 0 | 6 | 2 | 0 | 0 | 2 (25%) | 2 (25%) | 0 |
| TEC Technology & Platforms | 8 | 0 | 1 | 5 | 2 | 0 | 0 | 2 (25%) | 2 (25%) | 0 |
| SEC AI Security | 6 | 0 | 1 | 4 | 0 | 1 | 0 | 1 (17%) | 1 (17%) | 0 |
| PPL People & Skills | 8 | 0 | 3 | 5 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 0 |
| CUL Culture & Change | 7 | 1 | 1 | 5 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 1 |
| MON Measure & Improve | 9 | 0 | 4 | 5 | 0 | 0 | 0 | 0 (0%) | 0 (0%) | 0 |

## Targets below the baseline

These do not change the baseline result.

| Control | Target | Rationale | Approved by | Review date |
|---|---|---|---|---|
| POR-08 Reuse across the organisation | 2 | Three uses and one build team: a reuse catalogue would cost more than it saves. Raise to 3 when a second team builds AI. | Chief Operating Officer (R. Pellow), Executive Committee, 4 November 2026 | 2027-11-30 |
| OPM-08 Collaboration and sharing | 2 | A small body gets most of the value by joining existing peer groups and sharing lessons informally, without a formal partnership approach. | Chief Operating Officer (R. Pellow), Executive Committee, 4 November 2026 | 2027-11-30 |
| PPL-03 Specialist roles and careers | 2 | A body of this size can use the cross-government profession framework for role profiles rather than build its own career paths and community. | Chief Operating Officer (R. Pellow), Executive Committee, 4 November 2026 | 2027-11-30 |
| CUL-08 Public and customer trust | 2 | Uses are internal or low visibility, so asking the existing industry stakeholder panel about the triage classifier is a proportionate first step. Raise to 3 if public-facing AI is planned. | Chief Operating Officer (R. Pellow), Executive Committee, 4 November 2026 | 2027-11-30 |

## Roadmap: 85 controls below target

In dependency order: a control's dependencies come before it. Combine with risk, legal deadlines and effort when planning; agreed actions, owners and dates are recorded on the Roadmap sheet.

| Step | Control | Now | Target | Criteria not met | Action | Owner | Due |
|---|---|---|---|---|---|---|---|
| 1 | STR-05 Horizon scanning and external expectations | 2 | 3 | STR-05.1, STR-05.2, STR-05.4 |  | ai governance lead |  |
| 1 | GOV-02 Executive accountability | 2 | 3 | GOV-02.2, GOV-02.3 |  | executive sponsor |  |
| 1 | TEC-02 Reference architecture for AI | 1 | 3 | TEC-02.1, TEC-02.2, TEC-02.3, TEC-02.4, TEC-02.5, TEC-02.6, TEC-02.7 |  | delivery lead |  |
| 1 | PPL-02 Leadership capability | 2 | 3 | PPL-02.1, PPL-02.2 |  | people lead |  |
| 1 | PPL-04 Skills assessment | 1 | 3 | PPL-04.1, PPL-04.2, PPL-04.3, PPL-04.4 |  | people lead |  |
| 2 | STR-01 AI ambition aligned to organisational strategy | 2 | 3 | STR-01.1, STR-01.2, STR-01.3 |  | executive sponsor |  |
| 2 | STR-07 Stakeholder input to strategy | 0 | 3 | STR-07.1, STR-07.2, STR-07.3 |  | executive sponsor |  |
| 2 | GOV-01 AI policy | 2 | 3 | GOV-01.1, GOV-01.2, GOV-01.3, GOV-01.4, GOV-01.5, GOV-01.6 | Add the legally banned practices to the draft, approve AI Policy v1.0 at the Executive Committee with an owner and review date, place it under document control and brief all staff | Head of Data (J. Okafor) | 2027-02-26 |
| 2 | GOV-04 Oversight forum | 2 | 3 | GOV-04.1, GOV-04.2, GOV-04.3, GOV-04.4 |  | ai governance lead |  |
| 2 | RSK-01 AI risk appetite | 1 | 3 | RSK-01.1, RSK-01.2, RSK-01.3 | Draft an AI risk appetite statement covering harm to people, legal, reputational and operational risk, with an owner and review date, for board approval | Head of Risk and Compliance (D. Fairbairn) | 2027-04-30 |
| 2 | RSK-04 Legal and regulatory obligations | 2 | 3 | RSK-04.1, RSK-04.2, RSK-04.3, RSK-04.4, RSK-04.5, RSK-04.6, RSK-04.7, RSK-04.8 |  | risk lead |  |
| 2 | OPM-01 Target operating model for AI | 1 | 3 | OPM-01.1, OPM-01.2, OPM-01.3, OPM-01.4, OPM-01.5 |  | executive sponsor |  |
| 2 | DAT-03 Data quality fit for purpose | 2 | 3 | DAT-03.1, DAT-03.2, DAT-03.3, DAT-03.4 |  | data owner |  |
| 2 | DAT-04 Finding and understanding data | 2 | 3 | DAT-04.1, DAT-04.2 |  | data owner |  |
| 2 | TEC-04 Integration with existing systems | 2 | 3 | TEC-04.2, TEC-04.3, TEC-04.4, TEC-04.5 |  | delivery lead |  |
| 2 | PPL-03 Specialist roles and careers | 1 | 2 | PPL-03.1, PPL-03.2, PPL-03.3, PPL-03.4 |  | people lead |  |
| 2 | PPL-07 Bringing in and keeping expertise | 2 | 3 | PPL-07.1, PPL-07.2, PPL-07.3 |  | people lead |  |
| 2 | MON-07 Re-assessing AI maturity | 1 | 3 | MON-07.1, MON-07.2, MON-07.3 |  | ai governance lead |  |
| 3 | STR-02 Where AI will and will not be used | 2 | 3 | STR-02.1, STR-02.2, STR-02.3, STR-02.4 |  | executive sponsor |  |
| 3 | STR-03 Investment and funding for AI | 2 | 3 | STR-03.1, STR-03.2, STR-03.3, STR-03.4 |  | executive sponsor |  |
| 3 | STR-04 Organisation-level value case | 1 | 3 | STR-04.1, STR-04.2, STR-04.3, STR-04.4 |  | executive sponsor |  |
| 3 | STR-08 Strategy review cycle | 0 | 3 | STR-08.1, STR-08.2, STR-08.3, STR-08.4 |  | executive sponsor |  |
| 3 | GOV-03 Decision rights proportionate to risk | 2 | 3 | GOV-03.1, GOV-03.2, GOV-03.3, GOV-03.4 |  | executive sponsor |  |
| 3 | GOV-06 AI inventory | 1 | 3 | GOV-06.1, GOV-06.2, GOV-06.3, GOV-06.4, GOV-06.5 | Build the AI inventory: Copilot, both pilots and AI features in bought products (HR and case management systems first), each with owners, risk tier, regulatory classification and suppliers | Head of Data (J. Okafor) | 2027-03-31 |
| 3 | GOV-08 Policy compliance and exceptions | 0 | 3 | GOV-08.1, GOV-08.2, GOV-08.3 |  | ai governance lead |  |
| 3 | GOV-10 Review and disclosure of AI-generated content | 2 | 3 | GOV-10.1, GOV-10.2, GOV-10.3 |  | ai governance lead |  |
| 3 | RSK-02 AI risk assessment method | 2 | 3 | RSK-02.1, RSK-02.2, RSK-02.3, RSK-02.4, RSK-02.5, RSK-02.6, RSK-02.7 |  | risk lead |  |
| 3 | RSK-05 Ethical principles in practice | 1 | 3 | RSK-05.1, RSK-05.2, RSK-05.3, RSK-05.4, RSK-05.5, RSK-05.6, RSK-05.7 |  | ai governance lead |  |
| 3 | POR-01 Idea intake open to all staff | 2 | 3 | POR-01.1, POR-01.2, POR-01.4, POR-01.5 |  | ai governance lead |  |
| 3 | POR-02 Agreed prioritisation criteria | 1 | 3 | POR-02.1, POR-02.2, POR-02.3, POR-02.4 |  | ai governance lead |  |
| 3 | OPM-02 Build, buy or configure approach | 1 | 3 | OPM-02.1, OPM-02.2, OPM-02.3, OPM-02.4 |  | delivery lead |  |
| 3 | OPM-06 Delivery standards for AI | 2 | 3 | OPM-06.1, OPM-06.2, OPM-06.3, OPM-06.4, OPM-06.5, OPM-06.6, OPM-06.7, OPM-06.8 |  | delivery lead |  |
| 3 | OPM-08 Collaboration and sharing | 1 | 2 | OPM-08.1, OPM-08.2, OPM-08.3, OPM-08.4 |  | executive sponsor |  |
| 3 | DAT-01 Data strategy supports AI | 2 | 3 | DAT-01.2, DAT-01.3, DAT-01.4, DAT-01.5 |  | data owner |  |
| 3 | DAT-05 Lawful and fair use of data | 2 | 3 | DAT-05.1, DAT-05.2, DAT-05.3, DAT-05.4, DAT-05.5, DAT-05.6 |  | data owner |  |
| 3 | DAT-06 Records management for AI | 2 | 3 | DAT-06.1, DAT-06.2, DAT-06.3 |  | data owner |  |
| 3 | TEC-01 Approved AI tools and platforms | 2 | 3 | TEC-01.1, TEC-01.2, TEC-01.3, TEC-01.4, TEC-01.5 |  | delivery lead |  |
| 3 | PPL-01 AI literacy for all staff | 2 | 3 | PPL-01.2, PPL-01.3, PPL-01.4, PPL-01.5, PPL-01.6 |  | people lead |  |
| 3 | CUL-01 Planned approach to AI change | 2 | 3 | CUL-01.1, CUL-01.2, CUL-01.3, CUL-01.4, CUL-01.5 |  | executive sponsor |  |
| 4 | STR-06 Multi-year AI roadmap tied to planning | 1 | 3 | STR-06.1, STR-06.2, STR-06.3, STR-06.4, STR-06.5 |  | executive sponsor |  |
| 4 | GOV-05 Named owners for each use of AI | 2 | 3 | GOV-05.1, GOV-05.2, GOV-05.3 |  | ai governance lead |  |
| 4 | GOV-07 Integration with existing governance | 2 | 3 | GOV-07.1, GOV-07.2, GOV-07.4, GOV-07.5 |  | ai governance lead |  |
| 4 | GOV-09 Public transparency about AI use | 1 | 3 | GOV-09.1, GOV-09.2, GOV-09.3, GOV-09.4, GOV-09.5, GOV-09.7 | Publish an algorithmic transparency record for the triage classifier before go-live, and record a publication decision for every inventory entry and impact assessment | Head of Data (J. Okafor) | 2027-01-15 |
| 4 | RSK-03 Impact assessment before deployment | 2 | 3 | RSK-03.1, RSK-03.2, RSK-03.3, RSK-03.4, RSK-03.5, RSK-03.6 | Complete and sign off an impact assessment for the triage classifier covering equality, privacy, rights, workforce and wider effects before go-live, then adopt the template for every use | Data Protection Officer (M. Achebe) | 2027-01-15 |
| 4 | RSK-07 Human oversight proportionate to risk | 2 | 3 | RSK-07.1, RSK-07.2, RSK-07.3 |  | business owner |  |
| 4 | RSK-09 Risk of AI from suppliers | 2 | 3 | RSK-09.1, RSK-09.2, RSK-09.3, RSK-09.4, RSK-09.5, RSK-09.6 |  | risk lead |  |
| 4 | POR-03 Pipeline register of proposed uses | 2 | 3 | POR-03.1, POR-03.2, POR-03.3 |  | ai governance lead |  |
| 4 | POR-04 Stage gates from idea to retirement | 2 | 3 | POR-04.1, POR-04.2, POR-04.3, POR-04.4, POR-04.5 |  | ai governance lead |  |
| 4 | POR-06 Safe experimentation | 2 | 3 | POR-06.1, POR-06.2, POR-06.3, POR-06.4, POR-06.5 |  | delivery lead |  |
| 4 | DAT-08 Provenance of training and test data | 2 | 3 | DAT-08.1, DAT-08.2, DAT-08.3 |  | data owner |  |
| 4 | SEC-01 AI security baseline | 2 | 3 | SEC-01.2, SEC-01.3, SEC-01.4, SEC-01.5 |  | security lead |  |
| 4 | PPL-05 Role-based learning | 2 | 3 | PPL-05.1, PPL-05.2, PPL-05.3, PPL-05.4, PPL-05.5, PPL-05.6, PPL-05.7 |  | people lead |  |
| 4 | PPL-06 Workforce planning for AI | 1 | 3 | PPL-06.1, PPL-06.2, PPL-06.3 |  | people lead |  |
| 4 | PPL-08 Support for staff using AI | 2 | 3 | PPL-08.1, PPL-08.2, PPL-08.4, PPL-08.5 |  | people lead |  |
| 4 | CUL-02 Internal communication about AI | 2 | 3 | CUL-02.1, CUL-02.2, CUL-02.3 |  | executive sponsor |  |
| 4 | CUL-03 Staff and representative engagement | 2 | 3 | CUL-03.1, CUL-03.2, CUL-03.4 |  | people lead |  |
| 4 | CUL-06 Champions and communities | 2 | 3 | CUL-06.1, CUL-06.2, CUL-06.3, CUL-06.4 |  | people lead |  |
| 4 | MON-05 Independent assurance reviews | 2 | 3 | MON-05.1, MON-05.2, MON-05.3, MON-05.4, MON-05.5, MON-05.6, MON-05.7 |  | risk lead |  |
| 5 | RSK-06 Fairness and bias management | 2 | 3 | RSK-06.1, RSK-06.2, RSK-06.3, RSK-06.4, RSK-06.5, RSK-06.6 |  | business owner |  |
| 5 | RSK-08 Explanation and challenge for affected people | 1 | 3 | RSK-08.1, RSK-08.2, RSK-08.3 | Add an AI notice to the correspondence acknowledgement and website contact page, and a route for a person to ask for their letter's routing to be reviewed | Head of Correspondence (L. Haddad) | 2027-01-15 |
| 5 | POR-05 Proportionate business case | 2 | 3 | POR-05.1, POR-05.2, POR-05.3 |  | business owner |  |
| 5 | POR-09 Retiring uses of AI | 1 | 3 | POR-09.1, POR-09.2, POR-09.3, POR-09.4, POR-09.5, POR-09.6 |  | business owner |  |
| 5 | OPM-04 AI-aware procurement and contracts | 2 | 3 | OPM-04.1, OPM-04.2, OPM-04.3, OPM-04.4, OPM-04.5, OPM-04.6, OPM-04.7, OPM-04.8 |  | delivery lead |  |
| 5 | OPM-07 Service management for live AI | 2 | 3 | OPM-07.1, OPM-07.2, OPM-07.3, OPM-07.4 |  | delivery lead |  |
| 5 | SEC-02 AI threat modelling | 2 | 3 | SEC-02.1, SEC-02.2, SEC-02.3, SEC-02.4, SEC-02.5 |  | security lead |  |
| 5 | SEC-03 Security of the AI supply chain | 2 | 3 | SEC-03.1, SEC-03.2, SEC-03.4, SEC-03.5, SEC-03.7, SEC-03.8 |  | security lead |  |
| 5 | SEC-05 AI in security incident response | 2 | 3 | SEC-05.1, SEC-05.2, SEC-05.3, SEC-05.4, SEC-05.5, SEC-05.7, SEC-05.8 |  | security lead |  |
| 5 | CUL-05 Learning from what did not work | 1 | 3 | CUL-05.1, CUL-05.2, CUL-05.3 |  | ai governance lead |  |
| 5 | CUL-07 Adoption support for affected teams | 2 | 3 | CUL-07.1, CUL-07.2, CUL-07.3 |  | business owner |  |
| 5 | CUL-08 Public and customer trust | 0 | 2 | CUL-08.1, CUL-08.2, CUL-08.3 |  | executive sponsor |  |
| 5 | MON-04 AI incidents and near misses | 1 | 3 | MON-04.1, MON-04.2, MON-04.3 | Define AI incidents and near misses, add an AI category to the service desk linked to security incident handling, and brief staff with the September 2026 Copilot case as the example | Head of Data (J. Okafor) | 2027-03-31 |
| 5 | MON-06 User feedback | 2 | 3 | MON-06.1, MON-06.2, MON-06.3 |  | business owner |  |
| 6 | OPM-03 Running cost management | 2 | 3 | OPM-03.2, OPM-03.3, OPM-03.5 |  | delivery lead |  |
| 6 | OPM-05 Supplier performance and exit | 2 | 3 | OPM-05.2, OPM-05.3 |  | delivery lead |  |
| 6 | OPM-09 Continuity when AI fails | 1 | 3 | OPM-09.1, OPM-09.2, OPM-09.3, OPM-09.4, OPM-09.5 |  | delivery lead |  |
| 6 | MON-01 Performance measures and baselines | 2 | 3 | MON-01.1, MON-01.2, MON-01.3, MON-01.4 |  | business owner |  |
| 6 | MON-09 Serious AI incidents and external notification | 1 | 3 | MON-09.1, MON-09.3, MON-09.5, MON-09.6, MON-09.7 |  | risk lead |  |
| 7 | POR-07 Pilot to production decisions | 2 | 3 | POR-07.1, POR-07.2 |  | business owner |  |
| 7 | TEC-06 Testing and evaluation before release | 2 | 3 | TEC-06.1, TEC-06.2, TEC-06.3, TEC-06.4, TEC-06.5, TEC-06.6, TEC-06.7, TEC-06.8 |  | delivery lead |  |
| 7 | MON-03 Benefits tracking | 1 | 3 | MON-03.1, MON-03.2, MON-03.3 |  | business owner |  |
| 8 | TEC-05 Managing models in live use | 2 | 3 | TEC-05.2, TEC-05.3, TEC-05.4, TEC-05.5, TEC-05.6, TEC-05.7 |  | delivery lead |  |
| 8 | SEC-06 Security testing of AI before release | 1 | 3 | SEC-06.1, SEC-06.2, SEC-06.3, SEC-06.4, SEC-06.5 | Commission security testing of the triage classifier against its threat model, including prompt injection through incoming letters and disclosure of personal data, by testers independent of the data team, before go-live | Head of Information Assurance (S. Lindqvist) | 2027-01-08 |
| 9 | TEC-07 Technology change and refresh | 2 | 3 | TEC-07.1, TEC-07.2, TEC-07.3, TEC-07.4 |  | delivery lead |  |
| 9 | MON-02 Monitoring live AI | 2 | 3 | MON-02.1, MON-02.2, MON-02.3, MON-02.4, MON-02.5, MON-02.6, MON-02.7 |  | delivery lead |  |
| 10 | MON-08 Reporting to leadership | 2 | 3 | MON-08.1, MON-08.2, MON-08.4 |  | executive sponsor |  |

## Insufficient evidence

- OPM-10 Involving people in AI design and evaluation
- CUL-04 Safe to raise concerns

## Low confidence results

- STR-05 Horizon scanning and external expectations
- OPM-05 Supplier performance and exit
- OPM-10 Involving people in AI design and evaluation
- CUL-04 Safe to raise concerns
- CUL-06 Champions and communities

## Strengths (Level 4 or above)

- SEC-04 Preventing information leakage through AI (Level 4)

## Data quality

- No problems found.
