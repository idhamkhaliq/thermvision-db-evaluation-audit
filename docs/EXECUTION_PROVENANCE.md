# Execution provenance

The Paper 1 experiments were executed under a frozen protocol. This public repository preserves the machine-readable result exports, lock files, checkpoint identities, and verification code needed to audit the reported manuscript values.

## Recorded execution notebook identities

The project record preserves the following notebook identities/hashes. The raw notebook files are not part of the current repository package because their original `.ipynb` bytes are not available on the active project file surface; they must not be silently reconstructed and presented as the executed originals.

| Notebook / execution artifact | Recorded SHA256 | Role |
|---|---|---|
| `Paper1_Main_Frozen_Embedding_Extraction_v1.ipynb` | `d2d9e1491349fc71678a76bde28bf2ce43eba526c750a927e4ea54d01e14ff9e` | frozen ArcFace embedding extraction |
| `Paper1_Robustness_E_AdaFace_IR50_v1.ipynb` | `b5bed9e6ce2a04225bd9dde7c8b6b690d70d5e08d6cf699e6e13f6d7a27a598a` | AdaFace IR-50 robustness probe |
| `Paper1_B2G_Defensive_Completion_v1.ipynb` | `9d918e637f1e6557fd3cc8803747d1b043327efa48b750fadbb970a86224e14a` | B2-G geometry completion |

The authoritative final result ZIP hashes recorded in the project registry are:

- `Paper1_Confirmatory_Results_v1.zip`: `66b793dfff4b7aa68a7a523b7831d6108f79217d574d5a79f7c611ac186c47f6`
- `Paper1_B2G_Defensive_Results_v2.zip`: `e64aa90e7b4623a4de107e6125f7e06bad84f91b87a07360964863e64ed31004`
- `Paper1_Robustness_E_AdaFace_Results_v1_1.zip`: `a8793adfbe40ace1f1b746a8a5a081b691583a026d803d17996e1d084bee1237`

The extracted members included in this repository are checked by `REPOSITORY_SHA256SUMS.txt` and `scripts/verify_repository.py`.
