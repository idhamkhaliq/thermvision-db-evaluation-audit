# Reproducibility scope

This repository supports the manuscript:

**Protocol Sensitivity in Synthetic Thermal Video Face Recognition: An Evaluation Audit of ThermVision-DB**

The repository is designed for **result verification and provenance auditing**. It contains frozen machine-readable result exports and scripts that recompute/verify the main reported summary quantities from those exports.

It does not contain raw ThermVision-DB videos, pretrained recognition weights, or the original execution notebooks whose byte-level hashes are recorded in `docs/EXECUTION_PROVENANCE.md`.

## Frozen analysis boundary

- Evaluation corpus: 50 synthetic identities, 100 videos.
- Inferential unit: identity (`N = 50`).
- Primary frame budget: `B = 16`.
- Defensive budgets: `B = 8` and `B = 32`.
- Primary probe: frozen ArcFace `w600k_r50.onnx`.
- Secondary robustness probe: frozen AdaFace IR-50 / MS1MV2.
- No recognition model was fitted on ThermVision-DB identities.
- Set 1 and Set 2 are treated as generated sequence/condition templates, not independent real-sensor sessions.

## Primary audit axes

- **Audit A:** same-sequence versus strict cross-sequence template construction.
- **Audit B:** identity predictiveness after face-area replacement (context/background proxy; not pure-background isolation).
- **Audit C:** uniform versus contiguous temporal sampling under matched frame budgets.

## Verification

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements-verification.txt
python scripts/verify_repository.py
python scripts/verify_reported_results.py
```

The scripts operate only on the exported CSV/JSON files included in this repository.
