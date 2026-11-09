"""Validate the AI Adoption Controls Framework source (framework/meta.yaml + framework/domains/*.yaml).

Checks every rule agreed in Phase 0 (D0.3 to D0.6) so a bad record never reaches an output:
  - each domain file names a domain listed in meta.yaml, and its file name matches
  - IDs are DOM-NN, match their domain, and are unique across the whole framework
  - every required field is present and non-empty; levels 1 to 5 all defined; 2 to 4 questions
  - owner roles, lifecycle stages, applicability and status come from meta.yaml
  - dependencies point to real IDs (IDs in domains not yet drafted are warnings) and contain no cycles
  - mappings are {source, ref} with a known source and a ref matching that source's pattern
  - writing voice: no em or en dashes, and no spaced hyphens used as separators

Exit code 0 if no errors (warnings allowed), 1 otherwise. Used by every build script.

    python3 validate.py
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent / "framework"
REQUIRED = ["id", "title", "objective", "rationale", "levels", "questions", "evidence", "owner", "lifecycle",
            "applicability", "dependencies", "mappings", "status", "version"]
ID_RE = re.compile(r"^([A-Z]{3})-(\d{2})$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
DASHES = re.compile(r"[–—]| - ")


def load():
    meta = yaml.safe_load((ROOT / "meta.yaml").read_text(encoding="utf-8"))
    domains = {}
    for f in sorted((ROOT / "domains").glob("*.yaml")):
        domains[f.name] = yaml.safe_load(f.read_text(encoding="utf-8"))
    return meta, domains


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def validate(meta, domains):
    errors, warnings = [], []
    known_domains = meta["domains"]
    roles, stages = set(meta["owner_roles"]), set(meta["lifecycle_stages"])
    applic, statuses, sources = set(meta["applicability"]), set(meta["statuses"]), meta["sources"]
    all_ids, deps = {}, {}

    for fname, d in domains.items():
        code = d.get("domain")
        if code not in known_domains:
            errors.append(f"{fname}: domain '{code}' is not in meta.yaml")
            continue
        if known_domains[code]["file"] != fname:
            errors.append(f"{fname}: meta.yaml expects domain {code} in {known_domains[code]['file']}")
        for c in d.get("controls") or []:
            cid = c.get("id", "?")
            where = f"{fname} {cid}"
            for k in REQUIRED:
                if k not in c or (c[k] in (None, "", {}) and k not in ("dependencies", "mappings")):
                    errors.append(f"{where}: missing or empty '{k}'")
            m = ID_RE.match(cid)
            if not m:
                errors.append(f"{where}: ID must look like DOM-NN")
            elif m.group(1) != code:
                errors.append(f"{where}: ID prefix does not match domain {code}")
            if cid in all_ids:
                errors.append(f"{where}: duplicate ID (also in {all_ids[cid]})")
            all_ids[cid] = fname
            lv = c.get("levels") or {}
            if sorted(int(k) for k in lv) != [1, 2, 3, 4, 5]:
                errors.append(f"{where}: levels must define exactly 1 to 5 (level 0 is generic, in meta.yaml)")
            q = c.get("questions") or []
            if not 2 <= len(q) <= 4:
                errors.append(f"{where}: needs 2 to 4 questions, has {len(q)}")
            own = c.get("owner") or {}
            if own.get("accountable") not in roles:
                errors.append(f"{where}: accountable owner '{own.get('accountable')}' not in meta.yaml owner_roles")
            for r in own.get("contributors") or []:
                if r not in roles:
                    errors.append(f"{where}: contributor '{r}' not in meta.yaml owner_roles")
            for s in c.get("lifecycle") or []:
                if s not in stages:
                    errors.append(f"{where}: lifecycle stage '{s}' not in meta.yaml")
            if c.get("applicability") not in applic:
                errors.append(f"{where}: applicability '{c.get('applicability')}' not in meta.yaml")
            if c.get("status") not in statuses:
                errors.append(f"{where}: status '{c.get('status')}' not in meta.yaml")
            if not SEMVER.match(str(c.get("version", ""))):
                errors.append(f"{where}: version must be x.y.z")
            for mp in c.get("mappings") or []:
                src, ref = mp.get("source"), str(mp.get("ref", ""))
                if src not in sources:
                    errors.append(f"{where}: mapping source '{src}' not in meta.yaml")
                elif not re.match(sources[src]["ref_pattern"], ref):
                    errors.append(f"{where}: mapping ref '{ref}' does not match the {src} pattern")
            crit = c.get("criteria")
            if crit is None:
                warnings.append(f"{where}: no Level 3 criteria yet (v1.0, review theme D)")
            else:
                if not 1 <= len(crit) <= 8:
                    errors.append(f"{where}: needs 1 to 8 Level 3 criteria, has {len(crit)}")
                for i, cr in enumerate(crit, 1):
                    if cr.get("id") != f"{cid}.{i}":
                        errors.append(f"{where}: criterion {i} must have id {cid}.{i}, has {cr.get('id')}")
                    ap = cr.get("applies", "core")
                    aps = [ap] if isinstance(ap, str) else list(ap)
                    for a in aps:
                        if a != "core" and a not in (meta.get("overlays") or {}):
                            errors.append(f"{where}: criterion {cr.get('id')} applies to unknown overlay '{a}'")
                    if not cr.get("text"):
                        errors.append(f"{where}: criterion {cr.get('id')} has no text")
            gd = c.get("guidance")
            if gd is None:
                warnings.append(f"{where}: no implementation guidance yet (Phase 3, D3.3)")
            else:
                for k, lo, hi in (("steps", 3, 5), ("pitfalls", 1, 3), ("artefacts", 1, 4)):
                    if not lo <= len(gd.get(k) or []) <= hi:
                        errors.append(f"{where}: guidance {k} needs {lo} to {hi} items, has {len(gd.get(k) or [])}")
            deps[cid] = list(c.get("dependencies") or [])
            for text in strings({k: c.get(k) for k in ("title", "objective", "rationale", "levels", "questions",
                                                       "evidence", "guidance", "criteria")}):
                if DASHES.search(text):
                    errors.append(f"{where}: dash used as a separator (writing voice): '{text[:60]}'")

    # retired controls: must point to a live replacement; nothing live may depend on them
    status_of = {c["id"]: c.get("status") for d in domains.values() for c in d.get("controls") or []}
    for d in domains.values():
        for c in d.get("controls") or []:
            if c.get("status") == "retired":
                rb = c.get("replaced_by")
                if rb and status_of.get(rb) in (None, "retired"):
                    errors.append(f"{c['id']}: replaced_by {rb} does not exist or is itself retired")
            elif "replaced_by" in c:
                errors.append(f"{c['id']}: replaced_by is only allowed on retired controls")
    for cid, ds in deps.items():
        if status_of.get(cid) != "retired":
            for t in ds:
                if status_of.get(t) == "retired":
                    errors.append(f"{cid}: depends on retired control {t}")

    drafted = {d.get("domain") for d in domains.values()}
    for cid, ds in deps.items():
        for t in ds:
            if t == cid:
                errors.append(f"{cid}: depends on itself")
            elif t not in all_ids:
                m = ID_RE.match(t)
                if m and m.group(1) in known_domains and m.group(1) not in drafted:
                    warnings.append(f"{cid}: dependency {t} is in a domain not drafted yet")
                else:
                    errors.append(f"{cid}: dependency {t} does not exist")

    # cycle check (depth-first)
    state = {}

    def visit(n, path):
        if state.get(n) == 1:
            errors.append("dependency cycle: " + " -> ".join(path + [n]))
            return
        if state.get(n) == 2 or n not in deps:
            return
        state[n] = 1
        for t in deps[n]:
            visit(t, path + [n])
        state[n] = 2

    for n in deps:
        visit(n, [])

    undrafted = [k for k in known_domains if k not in drafted]
    return errors, warnings, all_ids, undrafted


STRENGTHS = {"direct", "partial"}


def load_mappings():
    """Phase 2: one file per source in framework/mappings/. Source of truth for mappings (D0.4 field is derived)."""
    out = {}
    d = ROOT / "mappings"
    if d.is_dir():
        for f in sorted(d.glob("*.yaml")):
            out[f.name] = yaml.safe_load(f.read_text(encoding="utf-8"))
    return out


def item_status(item):
    """covered = at least one direct; partial = only partial; gap = no controls, or flagged 'gap:' in the note."""
    note = str(item.get("note") or "")
    if not item.get("controls") or note.startswith("gap:"):
        return "gap" if not note.startswith("out of scope:") else "out of scope"
    return "covered" if any(c.get("strength") == "direct" for c in item["controls"]) else "partial"


def validate_mappings(meta, domains, mappings):
    errors, warnings = [], []
    status_of = {c["id"]: c.get("status") for d in domains.values() for c in d.get("controls") or []}
    sources = meta["sources"]
    seen_sources = {}
    for fname, m in mappings.items():
        src = (m or {}).get("source")
        if src not in sources:
            errors.append(f"mappings/{fname}: source '{src}' not in meta.yaml")
            continue
        if src in seen_sources:
            errors.append(f"mappings/{fname}: source {src} already mapped in {seen_sources[src]}")
        seen_sources[src] = fname
        refs = set()
        for it in m.get("items") or []:
            ref = str(it.get("ref", ""))
            where = f"mappings/{fname} {ref}"
            if ref in refs:
                errors.append(f"{where}: duplicate ref")
            refs.add(ref)
            if not re.match(sources[src]["ref_pattern"], ref):
                errors.append(f"{where}: ref does not match the {src} pattern")
            if not it.get("label"):
                errors.append(f"{where}: missing label")
            note = str(it.get("note") or "")
            ctrls = it.get("controls") or []
            if not ctrls and not (note.startswith("gap:") or note.startswith("out of scope:")):
                errors.append(f"{where}: no controls, so the note must start 'gap:' or 'out of scope:'")
            for c in ctrls:
                cid = c.get("id")
                if cid not in status_of:
                    errors.append(f"{where}: control {cid} does not exist")
                elif status_of[cid] == "retired":
                    errors.append(f"{where}: control {cid} is retired")
                if c.get("strength") not in STRENGTHS:
                    errors.append(f"{where}: {cid} strength '{c.get('strength')}' must be direct or partial")
            if ctrls and all(c.get("strength") == "partial" for c in ctrls) and not note:
                warnings.append(f"{where}: partial cover only, with no note saying what is missing")
            for text in (str(it.get("label", "")), note):
                if DASHES.search(text):
                    errors.append(f"{where}: dash used as a separator (writing voice): '{text[:60]}'")
    for d in domains.values():
        for c in d.get("controls") or []:
            if c.get("mappings"):
                warnings.append(f"{c['id']}: has inline mappings; mappings now live in framework/mappings/ (Phase 2)")
    return errors, warnings


def main():
    meta, domains = load()
    errors, warnings, ids, undrafted = validate(meta, domains)
    mappings = load_mappings()
    me, mw = validate_mappings(meta, domains, mappings)
    errors += me
    warnings += mw
    if mappings:
        items = [it for m in mappings.values() for it in (m.get("items") or [])]
        print(f"mappings: {len(mappings)} source file(s), {len(items)} items")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    retired = sum(1 for d in domains.values() for c in d.get("controls") or [] if c.get("status") == "retired")
    print(f"{len(ids) - retired} active controls ({retired} retired) in {len(domains)} domain file(s); "
          f"{len(errors)} errors, {len(warnings)} warnings; not drafted yet: {', '.join(undrafted) or 'none'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
