# Roadmap

Updated 2026-11-11. Also on the website: https://aacf.adriansaxton.com/roadmap/

What is planned for the AI Adoption Controls Framework. Each item has an issue for discussion; ideas for new items are welcome in [Discussions](https://github.com/adriansaxton/AACF/discussions/categories/ideas).

Live board: https://github.com/orgs/adriansaxton/projects/1

## Now

- **Independent review of the mappings** ([#1](https://github.com/adriansaxton/AACF/issues/1)). A qualified reviewer is sampling the high-impact cross-references to check the controls and strengths assigned. Findings will be folded into a release, with the mapping files' reviewer and date updated. *In progress, target 1.2.*

## Next

- **AACF MCP server** ([#2](https://github.com/adriansaxton/AACF/issues/2)). A public, read-only MCP server so any AI assistant that supports MCP can look up controls, criteria and cross-references directly, for example "which controls cover ISO/IEC 42001 clause 6.1.2". It will serve the published release data and store nothing. *Planned.*

- **Cross-reference: OWASP Top 10 for LLM Applications** ([#3](https://github.com/adriansaxton/AACF/issues/3)). Map the OWASP Top 10 for LLM Applications to the security and technology controls, by risk ID, as a source for the detail the framework leaves to specialist security frameworks. *Planned, target 1.2.*

- **Cross-reference: OWASP Top 10 for Agentic Applications** ([#4](https://github.com/adriansaxton/AACF/issues/4)). Map the OWASP Top 10 for Agentic Applications to the agentic AI overlay criteria and the security controls, giving the agentic criteria a dedicated security source. *Planned, target 1.2.*

- **Lite version** ([#5](https://github.com/adriansaxton/AACF/issues/5)). A short baseline of about twenty foundation controls with a quick self-assessment and a simple result, as a front door to the full framework. *Planned.*

## Later

- **Cross-reference: CSA AI Controls Matrix** ([#6](https://github.com/adriansaxton/AACF/issues/6)). A cross-reference to the CSA AI Controls Matrix by control ID. Prepared, and waiting on permission from the Cloud Security Alliance to publish. *Waiting.*

- **Agentic AI: identity, delegation and limits** ([#7](https://github.com/adriansaxton/AACF/issues/7)). Further agentic criteria on the identity and credentials an agent holds, agents acting for other agents, and spending and resource limits. Theme A1 in what the framework does not cover. *Planned.*

- **Intellectual property beyond contracts** ([#8](https://github.com/adriansaxton/AACF/issues/8)). Criteria on using content the organisation does not own when prompting or grounding AI, and on the licence terms of open models and datasets it adopts. Theme A2. *Planned.*

- **Red-teaming in live use** ([#9](https://github.com/adriansaxton/AACF/issues/9)). Adversarial testing repeated while a system is live and after model or supplier changes, covering harms beyond security. Theme A3. *Planned.*

- **Effects on jobs and work design** ([#10](https://github.com/adriansaxton/AACF/issues/10)). Assessing how a use of AI changes roles before it is deployed, and planning redeployment or reskilling. Theme A4. *Planned.*

- **Environmental sustainability targets** ([#11](https://github.com/adriansaxton/AACF/issues/11)). An organisation-level target for AI's energy, compute and water use, reported to leadership, and supplier disclosure of footprint. Theme A5. *Planned.*

- **People at higher risk of harm** ([#12](https://github.com/adriansaxton/AACF/issues/12)). Specific care where AI affects children or other people at higher risk of harm, such as stricter approval or a person in the loop by default. Theme A6. *Planned.*
