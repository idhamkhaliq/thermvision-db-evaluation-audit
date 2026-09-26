#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "results" / "confirmatory"
A = ROOT / "results" / "adaface"
B = ROOT / "results" / "b2g"


def close(name: str, got: float, expected: float, atol: float = 5e-7) -> None:
    if not math.isclose(float(got), float(expected), abs_tol=atol, rel_tol=0.0):
        raise AssertionError(f"{name}: expected {expected}, got {got}")
    print(f"PASS {name}: {got:.10f}")


def main() -> None:
    cond = pd.read_csv(C / "condition_summary.csv").set_index("condition")
    primary = pd.read_csv(C / "primary_hypotheses.csv").set_index("hypothesis")
    bnull = pd.read_csv(C / "primary_B_null_summary.csv").iloc[0]
    geom = pd.read_csv(C / "identity_geometry_summary.csv").iloc[0]
    ids = pd.read_csv(C / "identity_level_outcomes.csv")

    # Direct exported-condition checks.
    close("ArcFace baseline Rank-1", cond.loc["A0_C0_B0", "rank1_identity_balanced"], 0.98)
    close("ArcFace baseline margin", cond.loc["A0_C0_B0", "margin_mean"], 0.227687785966537)
    close("ArcFace A1 margin", cond.loc["A1", "margin_mean"], 0.27469820838691483)
    close("ArcFace B2 Rank-1", cond.loc["B2", "rank1_identity_balanced"], 0.96)
    close("ArcFace C1 margin", cond.loc["C1", "margin_mean"], 0.17191709527671037)

    # Recompute paired identity-level effects from the exported per-identity table.
    wide = ids.pivot(index="identity_id", columns="condition", values="margin_identity")
    a_effect = (wide["A1"] - wide["A0_C0_B0"]).mean()
    c_effect = (wide["C1"] - wide["A0_C0_B0"]).mean()
    close("ArcFace A1-A0 paired margin", a_effect, 0.047010422420377826)
    close("ArcFace C1-C0 paired margin", c_effect, -0.05577069068982664)
    close("ArcFace A primary exported estimate", primary.loc["A", "estimate"], a_effect)
    close("ArcFace C primary exported estimate", primary.loc["C", "estimate"], c_effect)
    close("ArcFace B2 permutation-null mean", bnull["null_mean"], 0.0200514)
    close("ArcFace geometry within mean", geom["within_mean"], 0.9361813219039982)
    close("ArcFace geometry between mean", geom["between_mean"], 0.5029043378906369)
    close("ArcFace geometry delta", geom["delta_mean"], 0.43327698401336123)

    # AdaFace robustness checks.
    acond = pd.read_csv(A / "AdaFace_Robustness_E_Condition_Summary.csv").set_index("condition")
    acon = pd.read_csv(A / "AdaFace_Robustness_E_Key_Contrasts.csv").set_index("audit")
    close("AdaFace baseline Rank-1", acond.loc["A0_B0_C0", "rank1_identity_balanced"], 0.98)
    close("AdaFace baseline margin", acond.loc["A0_B0_C0", "margin_mean"], 0.21748366617941006)
    close("AdaFace A1-A0 margin", acon.loc["A", "estimate"], 0.06299980669609685)
    close("AdaFace B2-B0 margin", acon.loc["B", "estimate"], -0.10462901513052461)
    close("AdaFace C1-C0 margin", acon.loc["C", "estimate"], -0.09178354579711635)

    # Geometry completion structure check.
    b2g = pd.read_csv(B / "B2G_video_geometry_mean_std_100.csv")
    if len(b2g) != 100 or b2g["canonical_video_id"].nunique() != 100:
        raise AssertionError("B2-G per-video table does not contain exactly 100 unique canonical videos")
    print("PASS B2-G canonical-video coverage: 100/100")

    print("\nAll reported-result verification checks passed.")


if __name__ == "__main__":
    main()
