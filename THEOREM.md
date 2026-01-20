# Protocol: Theorem-Per-Repo Template Standard (v1)

## Tag
PROTOCOL

## Status
T1 (published standard)

## Statement
**Protocol.** Every VIREON claim that rises to the level of a theorem, proof, law, or algorithmic assertion is stored in its own repository created from this template, with:
1) a precise statement and locked definitions,
2) an explicit proof (or protocol justification),
3) a falsification target,
4) a reproducible verification harness when computation is used,
5) a tamper-evident proofpack manifest verified by CI.

## Assumptions / Scope
- Repositories are hosted under `https://github.com/a3fpro-lab`.
- Claims are categorized using the tier policy:
  - T1: proved + independently checkable
  - T2: proved, not fully verified
  - T3: conditional / evidence-based (e.g., RH-conditional)
- This template does not assert truth of any mathematical claim by itself; it standardizes packaging, verification, and review.

## Definitions (locked)
- **fold** = function/action
- **folding** = process
- **folded** = final state
- **proofpack** = a tamper-evident artifact bundle (inputs + code + outputs + manifest + hashes)

## Falsification target
This protocol is falsified if a repo created from this template can be modified (changing any file content) without either:
- changing the manifest hash list, or
- failing CI verification.

In other words: any undetected mutation of a claimed artifact is a protocol failure.
