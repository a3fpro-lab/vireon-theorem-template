# VIREON Theorem Repo Template (v1)

**Status:** PROTOCOL (T1)  
**Tag:** PROTOCOL  
**Scope:** Standard structure for theorem/proof repos: statement, proof, algorithms, code, and tamper-evident proofpack verification.

## What this repo is
This is the canonical template used to create one repo per theorem / proof / protocol in the VIREON system.

## Contents
- `THEOREM.md` — required claim metadata: statement, assumptions, definitions, falsification target
- `PROOF.md` — proof skeleton (or protocol rationale) with explicit steps
- `ALGO/` — algorithms and update rules (if any)
- `CODE/` — verifier / experiments (deterministic preferred)
- `PROOFPACK/` — tamper-evident artifact layer (manifest + outputs)
- `tools/` — manifest creation + verification tools
- `.github/workflows/` — CI verification

## Verify (CI-grade)
This repo is self-verifying via `PROOFPACK/MANIFEST.json`.

- Local verify:
  - `python tools/verify_manifest.py`
- Update manifest after edits:
  - `python tools/make_manifest.py`

## Credits
**Origin:** Inkwon Song Jr. (Creator of VIREON)
