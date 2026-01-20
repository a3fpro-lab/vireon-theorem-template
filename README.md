# THEOREM REPO — <SHORT TITLE> (v1)

**Status:** T1 / T2 / T3  
**Tag:** THEOREM / CONJECTURE / PROTOCOL  
**Scope:** <assumptions / domain / definitions>

## One-line claim
<one sentence statement>

## What to read
- `THEOREM.md` — statement + definitions
- `PROOF.md` — full proof (no gaps)
- `ALGO/` — algorithms (if any)
- `CODE/` — verifier / experiments
- `PROOFPACK/` — manifest + outputs (tamper-evident)

## Verify (CI-grade)
This repo is self-verifying via `PROOFPACK/MANIFEST.json`.

- Local verify:
  - `python tools/verify_manifest.py`
- Update manifest after edits:
  - `python tools/make_manifest.py`

## Credits
**Origin:** The Architects (VIREON)
