# AI adoption assessment: Westmere Standards Agency (fictional)

Assessed against AI Adoption Controls Framework version 1.1.2. Report generated from `westmere-assessment.xlsx`; results are recomputed from the levels and targets entered. This is a framework assessment, not a certification or legal compliance opinion.

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

## Standards you answer to

For each standard selected on the Profile sheet, an item's foundation is in place when every control mapped directly to it is at Level 3 or above. This shows readiness, not compliance: the mapping is the author's interpretation, and items with partial cover only must be checked against the source.

| Standard | Items | Foundation in place | Not yet | Not assessed | Partial cover only | Other |
|---|---|---|---|---|---|---|
| ISO/IEC 42001 | 65 | 0 | 47 | 1 | 17 | 0 |
| NIST AI RMF 1.0 | 72 | 0 | 46 | 1 | 25 | 0 |
| NIST AI 600-1 | 12 | 0 | 9 | 0 | 3 | 0 |
| EU AI Act | 31 | 0 | 17 | 0 | 13 | 1 |
| GDS AI Playbook | 10 | 0 | 10 | 0 | 0 | 0 |
| Algorithmic Transparency Recording Standard | 14 | 0 | 9 | 0 | 5 | 0 |
| AI Cyber Security Code of Practice | 51 | 2 | 31 | 0 | 18 | 0 |
| UK Data and AI Ethics Framework | 116 | 3 | 100 | 5 | 6 | 2 |

### ISO/IEC 42001: not yet in place (47)

| Ref | Item | Controls to lift |
|---|---|---|
| 4.2 | Identify interested parties and their requirements | STR-07 (now 0) |
| 4.3 | Define the scope of AI governance | GOV-01 (now 2) |
| 5.1 | Top management commitment and support | GOV-02 (now 2) |
| 5.2 | Set and communicate an AI policy | GOV-01 (now 2) |
| 5.3 | Make clear who does what in AI governance, and with what authority | GOV-02 (now 2), GOV-05 (now 2) |
| 6.1.1 | Address risks and opportunities; set AI risk criteria | RSK-01 (now 1) |
| 6.1.2 | Assess AI risks | RSK-02 (now 2) |
| 6.1.3 | Treat AI risks and justify the controls chosen | RSK-02 (now 2) |
| 6.1.4 | Have a process for AI system impact assessment | RSK-03 (now 2) |
| 6.2 | Set measurable AI objectives and plan to achieve them | STR-01 (now 2) |
| 7.1 | Provide the resources needed | STR-03 (now 2) |
| 7.2 | Ensure competence | PPL-04 (now 1), PPL-05 (now 2) |
| 7.3 | Ensure awareness of the policy and of each person's part in it | PPL-01 (now 2) |
| 7.4 | Plan internal and external communication | CUL-02 (now 2) |
| 7.5 | Keep governance records current, approved and findable | GOV-01 (now 2) |
| 8.1 | Plan and control operational processes | POR-04 (now 2) |
| 8.2 | Carry out AI risk assessments at planned intervals and on change | RSK-02 (now 2) |
| 8.3 | Implement the risk treatment plan | RSK-02 (now 2) |
| 8.4 | Assess the effects of each AI system on people and society | RSK-03 (now 2) |
| 9.1 | Check how well AI governance is working, using evidence | MON-01 (now 2), MON-02 (now 2) |
| 9.2 | Audit the management system internally | MON-05 (now 2) |
| 9.3 | Top management reviews the management system | MON-08 (now 2) |
| 10.1 | Improve continually | MON-07 (now 1) |
| A.2.2 | Document an AI policy | GOV-01 (now 2) |
| A.2.3 | Align the AI policy with other organisational policies | GOV-07 (now 2) |
| A.2.4 | Review the AI policy | GOV-01 (now 2) |
| A.3.2 | Define and allocate AI roles and responsibilities | GOV-05 (now 2) |
| A.4.3 | Document data resources | GOV-06 (now 1) |
| A.5.2 | A process to assess impacts on people and society | RSK-03 (now 2) |
| A.5.4 | Assess impacts on individuals and groups | RSK-03 (now 2) |
| A.5.5 | Weigh effects on society and the environment | RSK-03 (now 2) |
| A.6.1.3 | Defined processes for responsible design and development | OPM-06 (now 2) |
| A.6.2.4 | Verification and validation measures and criteria | TEC-06 (now 2) |
| A.6.2.6 | Operation and monitoring, repairs, updates and support | OPM-07 (now 2), MON-02 (now 2) |
| A.6.2.7 | Technical documentation for each kind of interested party | TEC-05 (now 2) |
| A.6.2.8 | Keep event logs, at least when in use | MON-02 (now 2) |
| A.7.2 | Data management processes for development | DAT-01 (now 2) |
| A.7.3 | Record how data is acquired and selected | DAT-08 (now 2) |
| A.7.4 | Data quality requirements met | DAT-03 (now 2) |
| A.7.5 | Record data provenance | DAT-08 (now 2) |
| A.7.6 | Criteria and methods for data preparation | DAT-08 (now 2) |
| A.8.2 | Give users the information they need | TEC-05 (now 2) |
| A.8.4 | A plan for telling users about incidents | MON-09 (now 1), MON-04 (now 1) |
| A.8.5 | Know and meet reporting obligations to interested parties | RSK-04 (now 2) |
| A.9.4 | Use AI only as intended | MON-02 (now 2) |
| A.10.2 | Allocate responsibilities with partners, suppliers and customers | OPM-04 (now 2) |
| A.10.3 | Suppliers align with the responsible approach | RSK-09 (now 2) |

### NIST AI RMF 1.0: not yet in place (46)

| Ref | Item | Controls to lift |
|---|---|---|
| GOVERN 1.1 | Understand, manage and document the legal and regulatory requirements for AI | RSK-04 (now 2) |
| GOVERN 1.3 | Scale risk management effort to the organisation's risk tolerance | RSK-02 (now 2), RSK-01 (now 1) |
| GOVERN 1.4 | Set up the risk management process through clear policies and procedures | RSK-02 (now 2) |
| GOVERN 1.6 | Keep an inventory of AI systems, resourced by risk priority | GOV-06 (now 1) |
| GOVERN 1.7 | Decommission and phase out AI systems safely | POR-09 (now 1) |
| GOVERN 2.1 | Document roles, responsibilities and lines of communication for AI risk | GOV-05 (now 2) |
| GOVERN 2.2 | Train staff and partners in AI risk management for their duties | PPL-05 (now 2) |
| GOVERN 2.3 | Executive leadership owns decisions about AI risk | GOV-02 (now 2) |
| GOVERN 3.1 | A diverse team informs AI risk decisions across the lifecycle | GOV-04 (now 2) |
| GOVERN 3.2 | Define roles for human-AI configurations and human oversight | RSK-07 (now 2) |
| GOVERN 4.2 | Teams document the risks and impacts of the AI they build or use and communicate them | RSK-02 (now 2), RSK-03 (now 2) |
| GOVERN 5.1 | Gather and act on outside feedback about individual and societal impacts | CUL-08 (now 0) |
| GOVERN 5.2 | Feed reviewed feedback regularly into system design and implementation | MON-06 (now 2) |
| GOVERN 6.1 | Policies for third-party AI risks, including intellectual property infringement | RSK-09 (now 2) |
| GOVERN 6.2 | Contingency plans for failures in high-risk third-party data or AI | OPM-09 (now 1) |
| MAP 1.3 | Document the organisation's mission and goals for AI | STR-01 (now 2) |
| MAP 1.4 | Define the business value, or re-evaluate it for existing systems | POR-05 (now 2) |
| MAP 1.5 | Set and document risk tolerances | RSK-01 (now 1) |
| MAP 2.2 | Document the system's knowledge limits and how people use and oversee its output | TEC-05 (now 2) |
| MAP 3.1 | Examine and document expected benefits | POR-05 (now 2) |
| MAP 3.3 | Specify and document the targeted scope of application | TEC-06 (now 2) |
| MAP 3.4 | Define and assess operator and practitioner proficiency | PPL-05 (now 2) |
| MAP 3.5 | Define, assess and document human oversight processes | RSK-07 (now 2) |
| MAP 5.1 | Judge the likelihood and size of each beneficial and harmful impact | RSK-03 (now 2) |
| MAP 5.2 | Regular engagement with AI actors and feedback on impacts | MON-06 (now 2) |
| MEASURE 1.3 | Independent assessors and outside experts take part in regular assessments | MON-05 (now 2) |
| MEASURE 2.3 | Measure performance against criteria in conditions like live use | TEC-06 (now 2) |
| MEASURE 2.4 | Monitor system behaviour in production | MON-02 (now 2) |
| MEASURE 2.5 | Show the system is valid and reliable and record limits on generalising | TEC-06 (now 2) |
| MEASURE 2.7 | Evaluate and document security and resilience | SEC-06 (now 1) |
| MEASURE 2.9 | Explain, validate and document the model and interpret output in context | TEC-02 (now 1) |
| MEASURE 2.10 | Examine and document privacy risk | RSK-03 (now 2), DAT-05 (now 2) |
| MEASURE 2.11 | Evaluate fairness and bias and document the results | RSK-06 (now 2) |
| MEASURE 2.12 | Assess the environmental impact of training and running AI | MON-01 (now 2) |
| MEASURE 2.13 | Evaluate whether the testing and evaluation methods themselves work | TEC-06 (now 2) |
| MEASURE 3.1 | Regularly identify and track existing, unexpected and emerging risks in live use | RSK-02 (now 2) |
| MEASURE 3.2 | Track risks that current metrics cannot measure | MON-01 (now 2) |
| MANAGE 1.1 | Decide whether the system meets its purpose and should proceed | POR-04 (now 2), POR-07 (now 2) |
| MANAGE 1.2 | Prioritise risk treatment by impact, likelihood and resources | RSK-02 (now 2) |
| MANAGE 1.3 | Plan and document responses to high-priority risks | RSK-02 (now 2) |
| MANAGE 2.2 | Sustain the value of deployed systems | MON-03 (now 1) |
| MANAGE 2.3 | Respond to and recover from a newly found risk | MON-09 (now 1), MON-04 (now 1) |
| MANAGE 2.4 | Assign responsibility and means to override, disengage or switch off a system | RSK-07 (now 2) |
| MANAGE 3.1 | Monitor third-party AI risks and benefits regularly and apply controls | RSK-09 (now 2) |
| MANAGE 4.1 | Run post-deployment monitoring with feedback, appeal, override, incident and change routes | MON-02 (now 2) |
| MANAGE 4.3 | Tell relevant parties and affected people about incidents and track them | MON-09 (now 1), MON-04 (now 1) |

### NIST AI 600-1: not yet in place (9)

| Ref | Item | Controls to lift |
|---|---|---|
| R2 | Confabulation; confident but false or invented output, including made up citations and reasoning | TEC-06 (now 2) |
| R3 | Dangerous, Violent, or Hateful Content; AI producing inciting, violent, self harm or hateful output, including when safeguards are bypassed | TEC-06 (now 2) |
| R4 | Data Privacy; leakage, misuse or inference of personal and sensitive data through AI training, prompts and outputs | DAT-05 (now 2), RSK-03 (now 2) |
| R6 | Harmful Bias or Homogenization; AI amplifying bias, performing worse for some groups or languages, or giving overly uniform output | RSK-06 (now 2) |
| R7 | Human-AI Configuration; people trusting AI too much or too little, treating it as human, or becoming emotionally reliant on it | RSK-07 (now 2), MON-01 (now 2) |
| R8 | Information Integrity; AI easing the spread of misleading content, synthetic media and impersonation | GOV-10 (now 2) |
| R9 | Information Security; attacks on AI such as prompt injection and data poisoning, and AI lowering the barrier to cyber attack | SEC-02 (now 2), SEC-01 (now 2), SEC-06 (now 1) |
| R10 | Intellectual Property; AI reproducing protected work, exposing trade secrets, or copying likeness or voice without permission | OPM-04 (now 2), DAT-08 (now 2), GOV-10 (now 2) |
| R12 | Value Chain and Component Integration; untraceable or poorly vetted third party models, data and components in AI systems | RSK-09 (now 2), SEC-03 (now 2), DAT-08 (now 2) |

### EU AI Act: not yet in place (17)

| Ref | Item | Controls to lift |
|---|---|---|
| Art 4 | Make sure staff and others who run or use AI on the organisation's behalf are sufficiently AI literate | PPL-01 (now 2) |
| Art 5 | Do not use AI for any prohibited practice | GOV-03 (now 2) |
| Art 6 | Work out whether each use of AI is high-risk under Annex I or Annex III, and record the reasoning | GOV-06 (now 1) |
| Art 26(2) | Give human oversight to people with the competence, training, authority and support to do it | RSK-07 (now 2) |
| Art 26(4) | Where it controls input data, make sure it is relevant and sufficiently representative for the intended purpose | DAT-03 (now 2) |
| Art 26(5) | Monitor operation, tell the provider and regulator of risks and suspend use, and report serious incidents | MON-09 (now 1), MON-02 (now 2) |
| Art 26(6) | Keep automatically generated logs under its control for at least six months, or longer where the law requires | DAT-06 (now 2) |
| Art 26(7) | Before using high-risk AI at work, inform workers' representatives and the workers affected | CUL-03 (now 2) |
| Art 26(8) | Public authority deployers register their use, and do not use a high-risk system missing from the EU database | RSK-09 (now 2) |
| Art 26(11) | Tell people when an Annex III high-risk system makes or helps make decisions about them | RSK-08 (now 1) |
| Art 49(3) | Public authority deployers register themselves and their use of an Annex III high-risk system before use | GOV-09 (now 1) |
| Art 50(1) | As provider, design AI that interacts with people so they are told it is AI | RSK-08 (now 1) |
| Art 50(2) | As provider of a generative system, mark outputs in a machine-readable way as AI generated | TEC-02 (now 1) |
| Art 50(3) | As deployer of emotion recognition or biometric categorisation, inform the people exposed to it | RSK-08 (now 1) |
| Art 50(4) | As deployer, disclose deep fakes and AI generated text published to inform the public | GOV-10 (now 2) |
| Art 73 | Report serious incidents to the authorities within the legal deadlines where the deployer must do so | MON-09 (now 1) |
| Art 86 | Give affected people a clear explanation of the AI's role and the main elements of a high-risk decision | RSK-08 (now 1) |

### GDS AI Playbook: not yet in place (10)

| Ref | Item | Controls to lift |
|---|---|---|
| P1 | You know what AI is and what its limitations are | PPL-01 (now 2) |
| P2 | You use AI lawfully, ethically and responsibly | RSK-04 (now 2), RSK-05 (now 1), DAT-05 (now 2) |
| P3 | You know how to use AI securely | SEC-01 (now 2), SEC-02 (now 2) |
| P4 | You have meaningful human control at the right stages | RSK-07 (now 2) |
| P5 | You understand how to manage the full AI life cycle | POR-04 (now 2) |
| P6 | You use the right tool for the job | OPM-02 (now 1) |
| P7 | You are open and collaborative | OPM-08 (now 1) |
| P8 | You work with commercial colleagues from the start | OPM-04 (now 2) |
| P9 | You have the skills and expertise needed to implement and use AI solutions | PPL-03 (now 1), PPL-05 (now 2), PPL-02 (now 2) |
| P10 | You use these principles alongside your organisation's policies and have the right assurance in place | GOV-07 (now 2), MON-05 (now 2), GOV-04 (now 2) |

### Algorithmic Transparency Recording Standard: not yet in place (9)

| Ref | Item | Controls to lift |
|---|---|---|
| Tier 1 Summary information | Give a plain, non-technical public summary of the tool, what it is and why it is used, with a web link and contact | GOV-06 (now 1) |
| Tier 2 Owner and responsibility | Say which organisation and team are responsible, who the senior owner is, and which suppliers were involved and on what terms | GOV-05 (now 2) |
| Tier 2 Description and rationale | Describe how the tool works, its users, scope and limits, its benefits, the process it replaced and the alternatives considered | TEC-05 (now 2) |
| Tier 2 Deployment context | Explain how the tool fits the wider process, how people review its output, how often it is used, the training needed and how the public can appeal | RSK-07 (now 2), RSK-08 (now 1) |
| Tier 2 Model specification | For each model the organisation trained, tuned or tested, give its name, version, task, inputs, outputs, design, test performance and datasets | TEC-06 (now 2), DAT-08 (now 2) |
| Tier 2 Development data specification | Describe the data used to develop the tool, its size, sensitive attributes, representativeness, cleaning, collection, storage and sharing | DAT-08 (now 2), DAT-03 (now 2), DAT-05 (now 2) |
| Tier 2 Operational data specification | Describe the data the tool uses in live operation, its sensitive attributes, processing, storage, access and sharing | DAT-06 (now 2) |
| Tier 2 Risks, mitigations and impact assessments | List the impact assessments done with dates and findings, and the key risks of the tool with their mitigations | RSK-03 (now 2), RSK-02 (now 2) |
| Scope supplier transparency | Tell suppliers from the start that this level of transparency is expected, and work with them so little is withheld for commercial reasons | OPM-04 (now 2) |

### AI Cyber Security Code of Practice: not yet in place (31)

| Ref | Item | Controls to lift |
|---|---|---|
| 1.1 | Include AI security content in the cyber security training programme, kept current and tailored to role (System Operators, Developers, Data Custodians) | PPL-05 (now 2) |
| 1.2 | Keep all staff aware of current AI security threats and vulnerabilities and their mitigations (System Operators, Developers, Data Custodians) | PPL-01 (now 2) |
| 2.1 | When deciding to create an AI system, document the business need with its AI security risks and mitigations (System Operators, Developers) | SEC-02 (now 2) |
| 2.3 | Keep documentation and an audit trail of the operation and lifecycle of models, data sets and prompts (Developers) | TEC-05 (now 2) |
| 2.4 | Assess the AI security risks of any external component through due diligence (Developers, System Operators) | SEC-03 (now 2) |
| 2.6 | Limit and risk assess the permissions an AI system is given on other systems and data sources (Developers, System Operators) | TEC-04 (now 2) |
| 3.1 | Analyse threats, including AI-specific attacks, and manage the security risks, reviewing on change (Developers, System Operators) | SEC-02 (now 2) |
| 3.2 | Pass on security threats the developer cannot resolve, from developer to operator and from operator to end-users (Developers, System Operators) | PPL-08 (now 2) |
| 3.4 | Monitor and review system infrastructure continuously according to risk appetite, accepting that residual risk remains (Developers, System Operators) | SEC-01 (now 2) |
| 4.1 | Build in and maintain the ability for humans to oversee the AI system (Developers, System Operators) | RSK-07 (now 2) |
| 4.2 | Design systems so humans can readily assess the outputs they are responsible for, for example through explainability (Developers) | TEC-02 (now 1) |
| 4.5 | Make end-users aware of the uses of the AI system that are prohibited (Developers, System Operators) | TEC-01 (now 2) |
| 5.1 | Keep a comprehensive inventory of AI assets and their interdependencies (Developers, System Operators, Data Custodians) | GOV-06 (now 1) |
| 5.3 | Tailor disaster recovery plans to attacks aimed at AI systems, able to restore a known good state (System Operators) | SEC-05 (now 2) |
| 6.4 | Implement and publish a clear, accessible vulnerability disclosure policy (Developers, System Operators) | SEC-05 (now 2) |
| 6.5 | Create, test and maintain an AI incident management plan and an AI recovery plan (Developers, System Operators) | SEC-05 (now 2) |
| 6.6 | Make sure contracts with cloud service providers support these infrastructure requirements (Developers, System Operators) | OPM-04 (now 2) |
| 7.1 | Follow secure software supply chain processes for AI model and system development (Developers, System Operators) | SEC-03 (now 2) |
| 7.3 | Re-run evaluations on released models the organisation intends to use (Developers, System Operators) | TEC-06 (now 2) |
| 7.4 | Tell end-users in an accessible way before models are updated (System Operators) | TEC-05 (now 2) |
| 8.2 | Document how publicly sourced training data was obtained, where from and how it is used (Developers) | DAT-08 (now 2) |
| 8.3 | Keep an audit log of changes to system prompts and other model configuration (Developers) | TEC-05 (now 2) |
| 9.1 | Security test every model, application and system before release to operators or users (Developers) | SEC-06 (now 1) |
| 9.2 | Test before deployment, with the developer's support and ideally independent security testers (System Operators) | SEC-06 (now 1) |
| 10.1 | Tell end-users accessibly where and how their data will be used, accessed and stored, including retraining and human review (System Operators; Developers to supply the information) | DAT-05 (now 2) |
| 10.2 | Give end-users accessible guidance on using and configuring the AI, with limitations, failure modes and security updates (System Operators; Developers to supply the information) | PPL-08 (now 2) |
| 10.3 | Support end-users and affected entities to contain and limit the impact of a cyber security incident, with the process agreed in contracts (Developers, System Operators) | SEC-05 (now 2) |
| 11.2 | Treat major AI system updates as a new version, with new security testing and evaluation (Developers) | SEC-06 (now 1) |
| 12.2 | Analyse logs to confirm models still produce the desired outputs and to detect anomalies, breaches, drift or poisoning (System Operators) | SEC-01 (now 2) |
| 12.4 | Monitor model and system performance over time to detect sudden or gradual changes that could affect security (System Operators, Developers) | MON-02 (now 2) |
| 13.2 | When decommissioning a model or system, involve data custodians and securely delete data and configuration (Developers, System Operators) | POR-09 (now 1) |

### UK Data and AI Ethics Framework: not yet in place (100)

| Ref | Item | Controls to lift |
|---|---|---|
| Transparency 1 | Explain the what, how and why of the project in plain language to non-experts | POR-05 (now 2) |
| Transparency 2 | Maintain detailed records of the project, including the decisions made in its design | POR-04 (now 2) |
| Transparency 3 | Make information about a project or tool publicly available | GOV-09 (now 1) |
| Transparency 4 | Use the ATRS if in mandatory scope; consider publishing a record even if not | GOV-09 (now 1) |
| Transparency 5 | Give appropriate disclosure when AI has been used to produce an output | GOV-10 (now 2) |
| Transparency 6 | Maintain records of all data sources, including collection methods, licences and preprocessing | DAT-08 (now 2) |
| Transparency 7 | Publish DPIAs and EIAs where possible | GOV-09 (now 1) |
| Transparency 8 | Maintain detailed records of all design decisions and assumptions behind a solution | POR-04 (now 2) |
| Transparency 9 | Create and regularly update assurance documentation such as model cards or data set cards | TEC-05 (now 2) |
| Transparency 11 | Build algorithmic tools with explainability in mind, to the degree the use case needs | TEC-02 (now 1) |
| Accountability 2 | Talk to the DPO and ensure they have the information, tools and authority to govern | GOV-07 (now 2) |
| Accountability 3 | Establish independent reviews to review and challenge data and AI decisions | MON-05 (now 2) |
| Accountability 4 | Clarify legal responsibilities across the data and AI supply chain for all parties | RSK-04 (now 2) |
| Accountability 5 | When buying a system, define detailed responsibilities and liability contractually | OPM-04 (now 2) |
| Accountability 6 | Publish accessible information on how the AI system works and why it is ethical and lawful | GOV-09 (now 1) |
| Accountability 7 | Have mechanisms for users to give feedback, report errors or contest decisions | MON-06 (now 2), RSK-08 (now 1) |
| Accountability 8 | Establish a human in the loop to oversee outputs in risky or high-impact uses | RSK-07 (now 2) |
| Accountability 9 | Identify who is responsible for AI outputs and decisions, including LLM tools | GOV-05 (now 2) |
| Fairness 1 | Define fairness for the project and how to measure it across its life cycle | RSK-06 (now 2) |
| Fairness 2 | Understand your users: groups most affected and links to protected characteristics | RSK-06 (now 2) |
| Fairness 3 | Consider proxies for protected characteristics and be transparent about their use | RSK-06 (now 2) |
| Fairness 4 | Complete an EIA and consider publishing it with the DPIA and ATRS record | RSK-03 (now 2), GOV-09 (now 1) |
| Fairness 5 | Include diverse views: consider diversity of the team and contracted third parties | OPM-06 (now 2) |
| Fairness 6 | Collect feedback and data throughout so the project stays fair and delivers benefits | MON-02 (now 2), MON-06 (now 2) |
| Fairness 7 | Regularly update your EIA | RSK-03 (now 2) |
| Privacy 1 | Involve information governance teams early in the project design process | GOV-07 (now 2) |
| Privacy 2 | Record purpose and benefit of data collection and use it to prevent scope creep | DAT-05 (now 2) |
| Privacy 3 | Embed privacy by design and default and undertake a DPIA | OPM-06 (now 2), RSK-03 (now 2) |
| Privacy 4 | Adopt data minimisation: collect and process the least data the purpose needs | DAT-05 (now 2) |
| Privacy 5 | Facilitate data subjects' rights to access and correction, with meaningful consent | DAT-05 (now 2) |
| Privacy 6 | Use privacy enhancing technologies such as anonymisation or synthetic data | DAT-05 (now 2) |
| Privacy 8 | Consider additional privacy risks AI brings, such as re-identification or leakage | RSK-03 (now 2) |
| Privacy 9 | Provide clear privacy notices and give users free choice to configure settings | DAT-05 (now 2) |
| Privacy 10 | Prepare for breaches with clear plans and assigned responsibilities | SEC-05 (now 2) |
| Privacy 11 | Plan for decommissioning: data archival or deletion at an appropriate time | POR-09 (now 1), DAT-06 (now 2) |
| Environmental sustainability 1 | Explore alternative solutions, including simple and low-energy options, before selecting | OPM-02 (now 1) |
| Environmental sustainability 2 | Consider reuse of existing models, favouring open-source models over retraining | OPM-02 (now 1) |
| Environmental sustainability 3 | Select suitable metrics for measuring and assessing environmental impact | MON-01 (now 2) |
| Environmental sustainability 4 | Evaluate sustainability credentials of third-party providers, including renewable energy use | RSK-09 (now 2) |
| Environmental sustainability 5 | Raise awareness of the environmental and social impact of digital technologies | PPL-01 (now 2) |
| Societal impact 1 | Write down project objectives in non-technical terms before choosing a technical solution | POR-05 (now 2) |
| Societal impact 3 | Complete an Equality Impact Assessment | RSK-03 (now 2) |
| Societal impact 4 | Use feedback mechanisms such as surveys and advisory boards to shape outcomes | MON-06 (now 2) |
| Societal impact 5 | Make sure you have meaningful human control at the right stages | RSK-07 (now 2) |
| Societal impact 6 | Continuously evaluate and improve the project, including decommissioning when no longer useful | POR-04 (now 2), POR-09 (now 1) |
| Safety 2 | Comply with security requirements and standards such as Secure by Design | SEC-01 (now 2) |
| Safety 3 | Apply data minimisation to limit the potential harms of a data breach | DAT-05 (now 2) |
| Safety 5 | Check for data quality, accuracy or reliability issues such as drift or poisoning | DAT-03 (now 2), MON-02 (now 2) |
| Safety 6 | Ensure human oversight and strategies to intervene, especially in high-risk uses | RSK-07 (now 2) |
| Safety 7 | Run rigorous testing to find failure modes, including red teaming | TEC-06 (now 2), SEC-06 (now 1) |
| Safety 8 | If the system cannot be made sufficiently safe, do not use it | GOV-03 (now 2) |
| Safety 9 | Use available resources, including courses on risks and ethics | PPL-01 (now 2) |
| Trade-offs 1 | Include stakeholder perspectives by engaging with affected communities | CUL-08 (now 0) |
| Trade-offs 2 | Consult legal and human rights frameworks so decisions align with standards | RSK-04 (now 2) |
| Trade-offs 3 | Balance proportionality and necessity | RSK-05 (now 1) |
| Trade-offs 5 | Establish mechanisms to monitor outcomes and adjust if necessary | MON-02 (now 2) |
| SAT 1.1 | Describe the problem you are trying to solve in non-technical terms | POR-05 (now 2) |
| SAT 1.2 | Describe the project purpose and user need | OPM-06 (now 2) |
| SAT 1.3 | Have you consulted your organisation's DPO? | DAT-05 (now 2) |
| SAT 1.4 | Have you consulted your organisation's data and information security teams? | GOV-07 (now 2) |
| SAT 1.5 | Are you using any personal or sensitive data? Consider the privacy impact | DAT-04 (now 2), DAT-05 (now 2) |
| SAT 1.6 | Have you conducted a DPIA, and how will identified risks be mitigated? | RSK-03 (now 2) |
| SAT 1.8 | What governance structures support safe, effective and responsible implementation? | GOV-04 (now 2), RSK-05 (now 1) |
| SAT 1.9 | How have you assigned responsibility for outcomes? Can owners make necessary changes? | GOV-05 (now 2), GOV-03 (now 2) |
| SAT 1.10 | What process documents project decisions and builds an evidence base for them? | POR-03 (now 2), POR-04 (now 2) |
| SAT 1.12 | How are you ensuring diversity and representation in your project team? | OPM-06 (now 2) |
| SAT 1.13 | Who are your users, and how might groups be impacted unequally? | RSK-03 (now 2), RSK-06 (now 2) |
| SAT 1.16 | Are you researching environmental impact, and is it shaping early decisions? | OPM-02 (now 1) |
| SAT 2.1 | How are you implementing safety principles from the start of your project? | OPM-06 (now 2) |
| SAT 2.2 | What processes assess and resolve data quality issues? | DAT-03 (now 2) |
| SAT 2.3 | How are you communicating the system's purpose, design and outcomes to stakeholders? | TEC-05 (now 2) |
| SAT 2.4 | How are you communicating with individuals about how their data is used? | DAT-05 (now 2) |
| SAT 2.5 | How will outputs be clearly explained and understood by stakeholders and users? | TEC-02 (now 1) |
| SAT 2.6 | What privacy enhancing methods have you integrated into your project? | DAT-05 (now 2) |
| SAT 2.7 | What plan is in place for fairness testing? | RSK-06 (now 2) |
| SAT 2.8 | How are you identifying and mitigating biases in your data sets? | RSK-06 (now 2), DAT-03 (now 2) |
| SAT 2.9 | How are diverse needs captured and integrated into prototype development? | RSK-03 (now 2) |
| SAT 2.10 | What would be the harm in not doing the project? | POR-05 (now 2) |
| SAT 2.11 | Consider trade-offs between ethical principles and alternatives. Why prioritise the chosen solution? | RSK-05 (now 1) |
| SAT 3.1 | How have you considered the accuracy, representativeness and completeness of your data set? | DAT-03 (now 2) |
| SAT 3.2 | How have you evaluated and addressed fairness in your AI system before going live? | RSK-06 (now 2) |
| SAT 3.3 | How are you ensuring accessibility for all users? | OPM-06 (now 2) |
| SAT 3.4 | How have you designed and tested human oversight mechanisms? | RSK-07 (now 2) |
| SAT 3.5 | Is documentation in place so others can replicate your process, results and outputs? | DAT-08 (now 2), TEC-05 (now 2) |
| SAT 3.6 | Have you checked whether the project is in scope of the ATRS? | GOV-09 (now 1) |
| SAT 3.8 | Could the project affect employment, working conditions or skills? Who gains or loses? | RSK-03 (now 2) |
| SAT 3.9 | What go or no-go criteria apply before going live, and what would cause delay? | POR-04 (now 2), GOV-03 (now 2) |
| SAT 3.10 | How will you transition to live, and who will own the system afterwards? | GOV-05 (now 2), OPM-07 (now 2) |
| SAT 4.1 | How are you monitoring performance in deployment and responding if it degrades or becomes unsafe? | MON-02 (now 2), OPM-09 (now 1) |
| SAT 4.2 | How are logs and documentation maintained to support investigations and transparency? | DAT-06 (now 2) |
| SAT 4.3 | What mechanisms let users submit feedback on system performance? | MON-06 (now 2) |
| SAT 4.4 | How are you actioning user feedback to improve the project? | MON-06 (now 2) |
| SAT 4.5 | Can the rationale for outputs be explained understandably to users and affected individuals? | RSK-08 (now 1) |
| SAT 4.6 | How are you notifying users they are interacting with AI rather than a human? | RSK-08 (now 1) |
| SAT 4.7 | If within mandatory scope, have you published an ATRS transparency record? | GOV-09 (now 1) |
| SAT 4.8 | How long will data be retained, and what justifies that period? | DAT-06 (now 2) |
| SAT 4.9 | What monitoring and interventions detect and prevent misuse of the system? | MON-02 (now 2) |
| SAT 4.10 | What procedures are in place to safely stop or retire the system? | OPM-09 (now 1), POR-09 (now 1) |
| SAT 4.11 | Will people affected by shutdown or replacement be told? What are the wider impacts? | POR-09 (now 1) |
| SAT 4.13 | What measures responsibly manage or recycle hardware and infrastructure? | POR-09 (now 1) |

Not selected: JSP 936 Part 1, MITRE AI Maturity Model, UNESCO AI Maturity Framework.

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
| 3 | GOV-10 Review and disclosure of AI-generated content | 2 | 3 | GOV-10.1, GOV-10.2, GOV-10.3, GOV-10.4 |  | ai governance lead |  |
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
| 5 | MON-04 AI incidents and near misses | 1 | 3 | MON-04.1, MON-04.2, MON-04.3, MON-04.4 | Define AI incidents and near misses, add an AI category to the service desk linked to security incident handling, and brief staff with the September 2026 Copilot case as the example | Head of Data (J. Okafor) | 2027-03-31 |
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
