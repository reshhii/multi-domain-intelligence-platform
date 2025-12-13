import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/cyber_incidents.csv")


def _load_df():
    if not CSV_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(CSV_PATH)


def incidents_by_severity():
    df = _load_df()
    if df.empty or "severity" not in df.columns:
        return {}
    return df["severity"].value_counts().to_dict()


def incidents_by_status():
    df = _load_df()
    if df.empty or "status" not in df.columns:
        return {}
    return df["status"].value_counts().to_dict()
