import pandas as pd

class CyberAnalyticsService:

    @staticmethod
    def compute_kpis(df: pd.DataFrame):
        total = len(df)
        open_incidents = len(df[df["status"] == "Open"])
        critical = len(df[df["severity"] == "Critical"])
        resolved = len(df[df["status"] == "Resolved"])

        resolution_rate = round((resolved / total) * 100, 2) if total > 0 else 0

        return {
            "total": total,
            "open": open_incidents,
            "critical": critical,
            "resolution_rate": resolution_rate
        }

    @staticmethod
    def risk_score(df: pd.DataFrame):
        score = 0
        score += len(df[df["severity"] == "Critical"]) * 3
        score += len(df[df["severity"] == "High"]) * 2
        score += len(df[df["status"] == "Open"]) * 1

        if score > 15:
            return "HIGH"
        elif score > 7:
            return "MEDIUM"
        return "LOW"

    @staticmethod
    def ai_insights(df: pd.DataFrame):
        insights = []

        if df.empty:
            return ["No incidents available for intelligent analysis."]

        if (df["severity"] == "Critical").sum() >= 3:
            insights.append(
                "⚠️ A high concentration of critical incidents has been detected. This indicates elevated organisational risk."
            )

        if (df["status"] == "Open").sum() > len(df) / 2:
            insights.append(
                "🚨 More than half of incidents remain open, suggesting possible delays in incident response."
            )

        if not insights:
            insights.append(
                "✅ Current incident levels appear stable with no immediate risk indicators."
            )

        return insights
