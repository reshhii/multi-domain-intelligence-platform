import pandas as pd
from db.database import DatabaseManager

def migrate():
    DatabaseManager.init_schema()
    with DatabaseManager.connect() as conn:
        cyber = pd.read_csv("data/cyber_incidents.csv")
        cyber.to_sql("cyber_incidents", conn, if_exists="replace", index=False)

        it = pd.read_csv("data/it_tickets.csv")
        it.to_sql("it_tickets", conn, if_exists="replace", index=False)

if __name__ == "__main__":
    migrate()
