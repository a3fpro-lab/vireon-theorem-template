# Justification: Why this template standard is required (v1)

## Objective
Prevent definition drift, result drift, and overclaiming by enforcing a single packaging/verification discipline across all VIREON claim repositories.

## Step 1 — Make claims atomic
One repository per claim forces:
- one scope,
- one statement,
- one falsification target,
- one verification harness (if needed).

This reduces ambiguity and prevents “blob” claims.

## Step 2 — Make artifacts tamper-evident
The `PROOFPACK/MANIFEST.json` records sha256 hashes for all tracked files.
If any tracked file changes, verification fails unless the manifest is intentionally regenerated.

## Step 3 — Make verification automatic
CI runs `python tools/verify_manifest.py` on every push/PR.
Therefore, any accidental or malicious change to tracked content is surfaced immediately.

## Conclusion
This template standard enforces reproducibility and integrity as a prerequisite for any public claim under the VIREON system.
