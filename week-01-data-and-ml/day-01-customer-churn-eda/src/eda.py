
from pathlib import Path
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Project paths
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "dataWA_Fn-UseC_-Telco-Customer-Churn.csv"
REPORTS = ROOT / "reports"

REPORTS.mkdir(parents=True, exist_ok=True)


def load_data(path: Path) -> pd.DataFrame:
    """Load the original customer dataset."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Download the CSV into the project's data/ folder."
        )

    return pd.read_csv(path)


def inspect_data(df: pd.DataFrame) -> dict:
    """Create a first-pass data-quality report."""
    report = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values_by_column": {
            col: int(count)
            for col, count in df.isna().sum().items()
        },
        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },
    }

    return report


def analyze_churn(df: pd.DataFrame) -> None:
    """Save churn summaries and exploratory charts."""
    required = {"Churn", "Contract", "tenure", "MonthlyCharges"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Required columns missing: {sorted(missing)}")

    # Standardize the target labels without changing the original data.
    churn = df["Churn"].astype("string").str.strip()
    valid = churn.isin(["Yes", "No"])

    if not valid.all():
        print("Warning: Unexpected or missing churn labels detected.")

    # Overall churn rate, excluding rows with invalid target labels.
    churn_rate = (
        churn[valid].eq("Yes").mean() * 100
        if valid.any()
        else np.nan
    )

    # Write a summary that can be reviewed later.
    summary = {
        "customers_with_valid_churn_labels": int(valid.sum()),
        "churn_rate_percent": (
            round(float(churn_rate), 2)
            if pd.notna(churn_rate)
            else None
        ),
    }

    with open(REPORTS / "churn_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    # Churn rate by contract type.
    segment_data = df.loc[valid, ["Contract"]].copy()
    segment_data["Churn"] = churn.loc[valid].to_numpy()

    contract_summary = (
        segment_data.groupby("Contract", dropna=False)["Churn"]
        .agg(
            customers="size",
            churned=lambda s: s.eq("Yes").sum(),
            churn_rate=lambda s: s.eq("Yes").mean() * 100,
        )
        .reset_index()
        .sort_values("churn_rate", ascending=False)
    )

    contract_summary.to_csv(
        REPORTS / "churn_by_contract.csv", index=False
    )

    # Chart 1: overall churn distribution.
    churn_counts = churn[valid].value_counts().reindex(
        ["No", "Yes"], fill_value=0
    )

    fig, ax = plt.subplots(figsize=(6, 4))
    churn_counts.plot(kind="bar", ax=ax)
    ax.set_title("Customer Churn Distribution")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Number of customers")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(REPORTS / "churn_distribution.png", dpi=150)
    plt.close(fig)

    # Chart 2: churn rate by contract type.
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(
        contract_summary["Contract"].astype(str),
        contract_summary["churn_rate"],
    )
    ax.set_title("Churn Rate by Contract Type")
    ax.set_xlabel("Contract")
    ax.set_ylabel("Churn rate (%)")
    ax.tick_params(axis="x", rotation=15)
    fig.tight_layout()
    fig.savefig(REPORTS / "churn_by_contract.png", dpi=150)
    plt.close(fig)

    # Explore tenure; this is descriptive, not predictive.
    df["tenure"].describe().to_csv(REPORTS / "tenure_summary.csv")

    print("\nOverall churn rate:", round(churn_rate, 2), "%")
    print("\nChurn by contract type:")
    print(contract_summary.to_string(index=False))
    print(f"\nReports saved to: {REPORTS}")


def main() -> None:
    df = load_data(DATA_PATH)

    print("Dataset shape:", df.shape)
    print("\nFirst five rows:")
    print(df.head().to_string(index=False))

    print("\nColumn information:")
    df.info()

    report = inspect_data(df)

    with open(REPORTS / "data_quality.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\nData-quality summary:")
    print(json.dumps({
        "rows": report["rows"],
        "columns": report["columns"],
        "duplicate_rows": report["duplicate_rows"],
        "columns_with_missing_values": sum(
            count > 0
            for count in report["missing_values_by_column"].values()
        ),
    }, indent=2))

    analyze_churn(df)


if __name__ == "__main__":
    main()
