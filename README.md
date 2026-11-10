<p align="center">
  <a href="https://aacf.adriansaxton.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/aacf-logo-dark.png">
      <img src="assets/aacf-logo.png" alt="AACF: AI Adoption Controls Framework" width="420">
    </picture>
  </a>
</p>

<p align="center">
  <strong>Controls, levels and cross-references for organisations adopting AI</strong><br>
  <a href="https://aacf.adriansaxton.com">Website</a> · <a href="https://aacf.adriansaxton.com/assess/">Self-assessment</a> ·
  <a href="https://aacf.adriansaxton.com/downloads/">Downloads</a> · <a href="CHANGELOG.md">Changelog</a>
</p>

# AI Adoption Controls Framework (AACF)

What an organisation needs in place to adopt AI well, who owns it, how far along it is, and how that lines up with
the standards it answers to.

This repository holds the framework itself: the source of every control, criterion and cross-reference. To browse it,
take the self-assessment or download the matrix, workbook and reference guide, use the website:
https://aacf.adriansaxton.com

## What is in it

- **93 controls in 11 domains**, each with an objective, five level descriptors (Level 3 is the foundation every
  organisation should have), numbered Level 3 criteria, assessment questions, expected evidence, an accountable
  owner, dependencies and guidance on reaching Level 3.
- **Six overlays** for criteria that apply only to some organisations: public body, provides AI to others, regulated
  or high-impact use, generative AI, agentic AI, builds or tunes its own models.
- **An assessor rulebook**, a statement of intended use and claims, and a register of what the framework does not
  cover (`framework/rulebook.md`, `framework/intended-use.md`, `framework/residual-gaps.md`).
- **Cross-references** to these sources (coverage of mapped items, not a compliance finding):
  - ISO/IEC 42001
  - NIST AI RMF 1.0
  - NIST AI 600-1
  - EU AI Act
  - GDS AI Playbook
  - Algorithmic Transparency Recording Standard
  - AI Cyber Security Code of Practice
  - JSP 936 Part 1
  - MITRE AI Maturity Model
  - UNESCO AI Maturity Framework
  - UK Data and AI Ethics Framework
- **A worked example** of a completed assessment (`examples/westmere/`, a fictional organisation).

## Repository layout

| Path | What |
|---|---|
| `framework/` | The source of truth: `meta.yaml`, `domains/*.yaml`, `mappings/*.yaml`, rulebook, intended use |
| `data/` | Every control in plain machine-readable form: `aacf.json` and `aacf-controls.csv` |
| `examples/westmere/` | Worked example (fictional organisation) |
| `_build/validate.py` | Checks the YAML against the framework's rules |

## Checking a change

```
pip install -r requirements.txt
python3 _build/validate.py
```

Edit the YAML in `framework/`. The validator checks IDs, required fields, levels, dependencies, cross-reference
formats and writing style, and must pass before a change is accepted.

## Using it

A result is a framework assessment, not certification or a legal compliance opinion. See
`framework/intended-use.md`.

## Feedback and contributions

Ideas and questions: [Discussions](https://github.com/adriansaxton/AACF/discussions). Something wrong, unclear or missing, or a
cross-reference that is over-claimed: [issues](https://github.com/adriansaxton/AACF/issues). See CONTRIBUTING.md.

## Licence

Content (everything except `_build/validate.py`): Creative Commons Attribution-ShareAlike 4.0 International. The
validator: MIT. The AACF name, logo and website design are not covered by these licences; see NOTICE.md.

Version 1.1.1. Copyright 2026 Adrian Saxton.
