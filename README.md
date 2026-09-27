# ThermVision-DB Evaluation Audit: Reproducibility Repository

Reproducibility and result-verification materials for:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22974338.svg)](https://doi.org/10.5281/zenodo.22974338)

> **Protocol Sensitivity in Synthetic Thermal Video Face Recognition: An Evaluation Audit of ThermVision-DB**

**Authors:** Idham Khaliq, Uturestantix

This repository accompanies a machine-vision evaluation study of protocol sensitivity in the synthetic thermal video face dataset ThermVision-DB. The study holds pretrained recognition probes fixed and audits how measured identity performance changes with sequence-template construction, residual visual information after face-area replacement, and temporal sampling.

## What is included

- frozen confirmatory result exports for the ArcFace probe;
- AdaFace IR-50 robustness result exports and lock files;
- B2-G geometry summaries;
- crop-QC metadata;
- baseline/provenance registries;
- SHA256 manifest for every file committed in the verification package;
- scripts that verify repository integrity and reproduce key manuscript values from the frozen exports.

## What is not included

- raw ThermVision-DB images/videos;
- pretrained ArcFace or AdaFace model weights;
- private credentials/tokens;
- the original execution notebooks whose hashes are documented but whose original bytes are not available in the active project file surface.

The repository therefore supports **verification of the reported frozen outputs**, not a claim that this package alone can regenerate every embedding from raw video.

## Dataset

ThermVision-DB must be obtained from the dataset authors:

- Dataset DOI: https://doi.org/10.57967/hf/7026
- Hugging Face: https://huggingface.co/datasets/MAli-Farooq/ThermVision-DB
- Dataset article: https://doi.org/10.1016/j.dib.2026.112506

See [`DATA_ACCESS.md`](DATA_ACCESS.md).

## Repository structure

```text
.
├── README.md
├── AUTHORS.md
├── CITATION.cff
├── DATA_ACCESS.md
├── REPRODUCIBILITY.md
├── requirements-verification.txt
├── scripts/
│   ├── verify_repository.py
│   └── verify_reported_results.py
├── provenance/
│   ├── baseline and execution-provenance records
│   ├── analysis checkpoint/provenance notes
│   ├── SHA256 provenance manifests
│   └── archived confirmatory adapter/manifest files
├── results/
│   ├── confirmatory/
│   ├── adaface/
│   ├── b2g/
│   └── crop_qc/
└── docs/
    └── EXECUTION_PROVENANCE.md
```

## Quick verification

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-verification.txt
python scripts/verify_repository.py
python scripts/verify_reported_results.py
```

Expected key checks include:

- ArcFace A1-A0 mean identity-margin effect: `+0.0470104`;
- ArcFace C1-C0 mean identity-margin effect: `-0.0557707`;
- ArcFace B2 identity-balanced Rank-1: `0.96` with permutation-null mean `0.0200514`;
- AdaFace A1-A0 margin effect: `+0.0629998`;
- AdaFace B2-B0 margin effect: `-0.1046290`;
- AdaFace C1-C0 margin effect: `-0.0917835`.

## Interpretation boundary

This repository does not establish validity on real thermal sensors, human populations, or independent acquisition sessions. The empirical conclusions are bounded to the finite ThermVision-DB benchmark and the frozen probes/evaluation constructions reported in the manuscript.

## Archived release

GitHub release `v0.1.0` is archived in Zenodo: **10.5281/zenodo.22974338** (https://doi.org/10.5281/zenodo.22974338).

## License

Project-controlled software in this repository is released under the **MIT License**. See [`LICENSE`](LICENSE) and [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md).

ThermVision-DB raw media are not redistributed here and remain governed by the upstream dataset terms. Third-party model weights and software retain their respective licenses.
