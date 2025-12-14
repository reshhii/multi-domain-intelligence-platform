import pandas as pd
from pathlib import Path


class ITOperationsAnalyticsService:
    DATA_PATH = Path("data/it_tickets.csv")

    @staticmethod
    def load_tickets():
        if not ITOperationsAnalyticsService.DATA_PATH.exists():
            return pd.DataFrame()

        df = pd.read_csv(ITOperationsAnalyticsService.DATA_PATH)

        # 🔐 Normalize column names (CRITICAL FIX)
        df.columns = df.columns.str.strip().str.lower()

        return df

    @staticmethod
    def ticket_kpis(df):
        # Ensure correct column casing
        df.columns = df.columns.str.lower()

        return {
            "Open Tickets": int((df["status"] == "Open").sum()),
            "In Progress": int((df["status"] == "In Progress").sum()),
            "Resolved": int((df["status"] == "Resolved").sum()),
            "Closed": int((df["status"] == "Closed").sum())
        }


    @staticmethod
    def ticket_trends(df):
        # Normalize columns 
        df = df.copy()
        df.columns = df.columns.str.strip().str.lower()

        if "created_at" not in df.columns:
            return pd.DataFrame()

        # Convert to datetime
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
        df = df.dropna(subset=["created_at"])

        if df.empty:
            return pd.DataFrame()

        # Group by month
        trend = (
            df
            .groupby(df["created_at"].dt.to_period("M"))
            .size()
            .reset_index(name="count")
        )

       # Convert period to string for plotting
        trend["date"] = trend["created_at"].astype(str)

        return trend[["date", "count"]]
