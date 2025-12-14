class ITTicket:
    def __init__(
        self,
        ticket_id,
        priority,
        description,
        status,
        assigned_to,
        created_at,
        resolution_time_hours
    ):
        self.ticket_id = ticket_id
        self.priority = priority
        self.description = description
        self.status = status
        self.assigned_to = assigned_to
        self.created_at = created_at
        self.resolution_time_hours = resolution_time_hours

    def to_dict(self):
        return {
            "Ticket ID": self.ticket_id,
            "Priority": self.priority,
            "Description": self.description,
            "Status": self.status,
            "Assigned To": self.assigned_to,
            "Created At": self.created_at,
            "Resolution Time (hrs)": self.resolution_time_hours
        }
