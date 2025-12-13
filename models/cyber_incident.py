class CyberIncident:
    def __init__(self, incident_id, timestamp, severity, category, status, description):
        self.incident_id = incident_id
        self.timestamp = timestamp
        self.severity = severity
        self.category = category
        self.status = status
        self.description = description

    def to_dict(self):
        return {
            "incident_id": self.incident_id,
            "timestamp": self.timestamp,
            "severity": self.severity,
            "category": self.category,
            "status": self.status,
            "description": self.description
        }

    def update_status(self, new_status):
        self.status = new_status
