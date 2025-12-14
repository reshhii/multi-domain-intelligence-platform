import pandas as pd

class AIInsightsService:

    @staticmethod
    def generate_insights(df: pd.DataFrame) -> dict:
        insights = {}

        if df.empty:
            insights["summary"] = "No incident data available for analysis."
            return insights

        # --- Severity Analysis ---
        severity_counts = df["severity"].value_counts()

        high_risk = severity_counts.get("High", 0) + severity_counts.get("Critical", 0)

        if high_risk > 0:
            insights["risk_level"] = "High Risk Environment"
            insights["risk_reason"] = (
                f"{high_risk} high or critical incidents detected. "
                "Immediate attention and mitigation strategies are recommended."
            )
        else:
            insights["risk_level"] = "Low Risk Environment"
            insights["risk_reason"] = (
                "No high or critical incidents detected. Current security posture is stable."
            )

        # --- Status Analysis ---
        open_cases = df[df["status"] == "Open"].shape[0]

        if open_cases > 5:
            insights["operational_health"] = "Backlog Detected"
            insights["operations_reason"] = (
                "A significant number of incidents remain open, indicating potential response delays."
            )
        else:
            insights["operational_health"] = "Operationally Healthy"
            insights["operations_reason"] = (
                "Incident response appears timely with manageable open cases."
            )

        # --- AI Recommendation ---
        insights["recommendation"] = (
            "Prioritize critical incidents, improve monitoring, "
            "and conduct regular security audits to reduce future risks."
        )

        return insights
