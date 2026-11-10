# What this framework does not cover

This register says plainly what the framework does not cover, or covers only in part. It was added after an
independent review asked for an explicit list of residual gaps and emerging risks. It has two parts:

- **Part A, themes:** areas of AI adoption that the controls do not yet address, or address only in part. These are
  judged by the author against the Level 3 criteria. Each one names what is in place today, what is missing and the
  likely route if it is taken up (a new criterion, a new control, an overlay, or leaving it to another framework).
- **Part B, mapped items:** items from the mapped standards that no control covers, or that are out of scope by
  design. It is generated from the cross-references, so it always matches them: see each standard's page.

An entry here is not a defect. Some gaps are deliberate, because the framework works at the level of the
organisation and leaves engineering detail to other frameworks. Others are candidates for a later version. The
register is reviewed at each release, and an entry closes only when a criterion or control covers it or the author
records a decision to leave it out.

## Part A: themes

Status key: **Partly addressed** = some criteria touch it, but an assessor could not use them to judge the whole
theme. **Not addressed** = no criterion covers it. **Out of scope by design** = deliberately left to another
framework or level.

### A1. Agentic AI beyond the first five criteria

- **Status:** Partly addressed.
- **In place:** the agentic overlay (AGT) adds five criteria: the inventory records each agent's tools and approval
  limits (GOV-06.6), actions are logged and a named person can stop an agent (MON-02.8), consequential actions need
  a person's approval (RSK-07.4), threat modelling covers hidden instructions and tool misuse (SEC-02.6), and testing
  tries to push an agent beyond its permissions (SEC-06.6).
- **Missing:** agents acting for or with other agents (delegation chains and multi-agent systems); the identity and
  credentials an agent holds, and how they are issued, limited and withdrawn; spending and resource limits; who is
  answerable when an agent acts in another organisation's systems.
- **Likely route:** further AGT criteria on agent identity and credentials, delegation and spending limits.
  Watch the EU AI Act guidance, NIST work on agent security, and the OWASP agentic AI material.

### A2. Intellectual property beyond contracts

- **Status:** Partly addressed.
- **In place:** contract terms cover rights in inputs and outputs and allocate liability (OPM-04.3, OPM-04.8); sharing
  and partnerships follow agreed IP terms (OPM-08.3, OPM-08.4); lawful use of data (DAT-05); from 1.1.0, review before
  release checks generative AI output for reproduced protected work and copied likeness or voice (GOV-10.4).
- **Missing:** rules on the organisation's own use of content it does not own when prompting or grounding AI; the same
  check for AI output that is not generative content; ownership of what staff create with
  AI; licence terms of open models and datasets the organisation adopts.
- **Likely route:** a criterion under TEC-01 or DAT-08 (model and dataset licences);
  possibly a BLD criterion on training data rights.

### A3. Red-teaming and testing in live use

- **Status:** Partly addressed.
- **In place:** security testing before release, independent for higher risk (SEC-06); harmful output testing and
  test-method review before release (TEC-06); monitoring of live AI (MON-02).
- **Missing:** adversarial testing repeated while a system is live, after model or supplier changes, and against
  harms other than security (for example persuasion, unsafe advice or misuse by users). No criterion uses the
  term red-teaming, so an assessor has nothing to point to.
- **Likely route:** a criterion under SEC-06 or MON-02 for periodic and change-triggered adversarial testing, scaled
  by risk (HIR, GEN).

### A4. Effects on jobs and work design

- **Status:** Partly addressed.
- **In place:** workforce planning for AI (PPL-06); staff and representative engagement (CUL-03); adoption support for
  affected teams (CUL-07); the environmental and social impact of AI in the literacy baseline (PPL-01.2).
- **Missing:** a commitment to assess how a use of AI changes roles before it is deployed, and to plan redeployment
  or reskilling; consultation duties where they apply.
- **Likely route:** a criterion under RSK-03 (impact assessment covers effects on staff) or PPL-06.

### A5. Environmental sustainability as a target

- **Status:** Partly addressed.
- **In place:** environmental footprint as a build, buy or configure criterion (OPM-02.2) and as a measure where it is
  material (MON-01.5); covered in the literacy baseline (PPL-01.2).
- **Missing:** an organisation-level target or budget for AI's energy, compute and water use, reported to leadership,
  and supplier disclosure of footprint.
- **Likely route:** a criterion under STR-04 or MON-08, and one under OPM-04 for supplier disclosure. Likely
  conditional rather than core.

### A6. People at higher risk of harm

- **Status:** Not addressed as a theme.
- **In place:** fairness and bias management (RSK-06); accessible explanation and notices (RSK-08, DAT-05.5,
  OPM-06.8); impact assessment (RSK-03).
- **Missing:** specific care where AI affects children or other people at higher risk of harm, such as stricter
  approval, safeguarding review or a person in the loop by default.
- **Likely route:** a criterion under RSK-03 or RSK-07, probably in the HIR overlay.

### A7. AI in physical and safety-critical settings

- **Status:** Partly addressed.
- **In place:** hazard analysis feeding the safety case where AI could contribute to physical harm (GOV-07.3, HIR).
- **Missing:** anything on AI embedded in physical equipment, robotics or operational technology beyond that
  hazard link. Sector safety regimes govern most of this.
- **Likely route:** leave to sector safety standards, and say so in the intended use. Revisit if a sector overlay is
  added.

### A8. Obligations on providers of general-purpose models

- **Status:** Out of scope by design.
- **Why:** the framework is for organisations adopting AI. Duties that fall on those who place general-purpose models
  on the market (for example under the EU AI Act) are detailed obligations for a small number of providers.
- **In place:** the BLD and PRV overlays cover building, tuning and offering AI to others at organisation level;
  single-supplier concentration is recorded as a risk (TEC-07.3).

### A9. Security engineering detail

- **Status:** Out of scope by design.
- **Why:** the security domain sets adoption-level objectives only. Detailed security controls for the AI supply
  chain, infrastructure and models are left to the CSA AI Controls Matrix and the UK AI Cyber Security Code of
  Practice. A cross-reference to the AI Controls Matrix is not included in this release.

### A10. Artefacts for each AI system

- **Status:** Out of scope by design.
- **Why:** the unit of assessment is the organisation. Where a standard asks for an artefact for each system (for
  example ISO/IEC 42001 Annex A documentation and logs), the framework requires the practice to exist and be governed,
  and an assessor samples uses. Mapped items affected are marked partial with a note.

### A11. Defence-specific requirements

- **Status:** Out of scope for core controls.
- **Why:** some JSP 936 requirements name defence bodies, standards, classification rules or the military meaning
  of meaningful human control. Neutral core controls cannot meet these. They stay in the JSP 936 cross-reference for a
  defence assessor.

## Part B: mapped items not covered

Each standard's page on the website, and the Coverage sheet of the controls matrix, list every mapped item with
its status. Items marked out of scope give the reason. At version 1.1.0 no mapped item of a published
cross-reference is a gap; six are out of scope: one EU AI Act item (law enforcement use of biometric
identification), three JSP 936 items (defence-specific standards and team assurance) and two UK Data and AI Ethics
Framework items (choice of explainability technique).

## Review log

| Date | Change |
|---|---|
| 1.1.0 | First published. Themes A1 to A11; A2 narrowed by GOV-10.4. |
