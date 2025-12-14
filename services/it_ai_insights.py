class ITAIInsights:

    @staticmethod
    def generate(df):
        open_tickets = (df["status"] == "Open").sum()
        high_priority = (df["priority"] == "High").sum()

        if open_tickets > 10:
            load = "High operational workload detected."
        else:
            load = "Operational workload is under control."

        if high_priority > 5:
            risk = "Critical support risk due to many high-priority tickets."
        else:
            risk = "Support risk level is normal."

        recommendation = (
            "Prioritize high-priority tickets and balance workload across support teams."
        )

        return {
            "load": load,
            "risk": risk,
            "recommendation": recommendation
        }
