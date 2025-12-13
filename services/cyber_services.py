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
                    row["incident_id"],
                    row["timestamp"],
                    row["severity"],
                    row["category"],
                    row["status"],
                    row["description"]
                )
            )

        return incidents

    @staticmethod
    def save_all(incidents):
        df = pd.DataFrame([i.to_dict() for i in incidents])
        df.to_csv(DATA_PATH, index=False)

    @staticmethod
    def add_incident(incident):
        incidents = CyberIncidentService.load_all()
        incidents.append(incident)
        CyberIncidentService.save_all(incidents)

    @staticmethod
    def update_incident_status(incident_id, new_status):
        incidents = CyberIncidentService.load_all()
        for incident in incidents:
            if incident.incident_id == incident_id:
                incident.update_status(new_status)
        CyberIncidentService.save_all(incidents)

    @staticmethod
    def delete_incident(incident_id):
        incidents = CyberIncidentService.load_all()
        incidents = [i for i in incidents if i.incident_id != incident_id]
        CyberIncidentService.save_all(incidents)
