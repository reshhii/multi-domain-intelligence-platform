import pandas as pd
from pathlib import Path
from models.cyber_incident import CyberIncident

DATA_PATH = Path("data/cyber_incidents.csv")


class CyberIncidentService:

    @staticmethod
    def load_all():
        if not DATA_PATH.exists():
            return []

        df = pd.read_csv(DATA_PATH)
        incidents = []

        for _, row in df.iterrows():
            incidents.append(
                CyberIncident(
                    incident_id=row["incident_id"],
                    timestamp=row["timestamp"],
                    severity=row["severity"],
                    category=row["category"],
                    status=row["status"],
                    description=row["description"]
                )
            )
        return incidents

    @staticmethod
    def add_incident(incident: CyberIncident):
        df = pd.read_csv(DATA_PATH) if DATA_PATH.exists() else pd.DataFrame()
        df = pd.concat([df, pd.DataFrame([incident.to_dict()])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

    @staticmethod
    def update_incident_status(incident_id, new_status):
        if not DATA_PATH.exists():
            return

        df = pd.read_csv(DATA_PATH)
        df.loc[df["incident_id"] == incident_id, "status"] = new_status
        df.to_csv(DATA_PATH, index=False)

    @staticmethod
    def delete_incident(incident_id):
        if not DATA_PATH.exists():
            return

        df = pd.read_csv(DATA_PATH)
        df = df[df["incident_id"] != incident_id]
        df.to_csv(DATA_PATH, index=False)
