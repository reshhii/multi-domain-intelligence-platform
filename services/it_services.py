import pandas as pd
from pathlib import Path
from models.it_ticket import ITTicket

DATA_PATH = Path("data/it_tickets.csv")


class ITTicketService:

    @staticmethod
    def load_all():
        if not DATA_PATH.exists():
            return []

        df = pd.read_csv(DATA_PATH)
        tickets = []

        for _, row in df.iterrows():
            ticket = ITTicket(
                ticket_id=row["ticket_id"],
                priority=row["priority"],
                description=row["description"],
                status=row["status"],
                assigned_to=row["assigned_to"],
                created_at=row["created_at"],
                resolution_time_hours=row["resolution_time_hours"]
            )
            tickets.append(ticket)

        return tickets


    @staticmethod
    def add_ticket(ticket: ITTicket):
        df = pd.read_csv(DATA_PATH) if DATA_PATH.exists() else pd.DataFrame()
        df = pd.concat([df, pd.DataFrame([ticket.to_dict()])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

    @staticmethod
    def update_ticket_status(ticket_id, new_status):
        df = pd.read_csv(DATA_PATH)
        df.loc[df["ticket_id"] == ticket_id, "status"] = new_status
        df.to_csv(DATA_PATH, index=False)

    @staticmethod
    def delete_ticket(ticket_id):
        df = pd.read_csv(DATA_PATH)
        df = df[df["ticket_id"] != ticket_id]
        df.to_csv(DATA_PATH, index=False)
