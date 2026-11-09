# Contributing

Feedback is the most useful contribution. Ideas for new controls, sources or features, and questions about using the
framework, are best raised in [Discussions](https://github.com/adriansaxton/AACF/discussions) (the Ideas category). Accepted ideas become
items on the roadmap, each with its own issue. Please open an issue for:

- a control, criterion or level descriptor that is wrong, unclear or missing;
- a cross-reference that is over-claimed (marked "direct" when the control only covers part of the item);
- a criterion that should be core rather than tied to an overlay, or the other way round;
- problems with the downloads or the website (the website itself is maintained separately; issues about it are
  welcome here).

Say which control or source item, what you think is wrong, and why.

## Change control

From v1.0.0, control IDs and criterion IDs are stable. A control is never renumbered and a retired ID is never
reused; retired controls stay in the data with a pointer to their replacement. Framework versions follow
MAJOR.MINOR.PATCH: a new or retired control, or a change to what Level 3 requires, is a MINOR release; wording or
mapping fixes that do not change requirements are a PATCH; a change to the scale or the structure is MAJOR. Each
release is listed in CHANGELOG.md. Changes to the website do not change the framework version.

## Pull requests

Edit the YAML in `framework/` and run `python3 _build/validate.py`; it must pass. Do not edit `data/`, which is
generated from the YAML at each release. By contributing you agree that your contribution is licensed under
CC BY-SA 4.0 (content) or MIT (the validator).
