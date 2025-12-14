import sqlite3
from pathlib import Path

DB_PATH = Path("db/platform.db")

class DatabaseManager:
    @staticmethod
    def connect():
        DB_PATH.parent.mkdir(exist_ok=True)
        return sqlite3.connect(DB_PATH)

    @staticmethod
    def init_schema():
        with DatabaseManager.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cyber_incidents (
                    incident_id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    severity TEXT,
                    category TEXT,
                    status TEXT,
                    description TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS it_tickets (
                    ticket_id INTEGER PRIMARY KEY,
                    priority TEXT,
                    description TEXT,
                    status TEXT,
                    assigned_to TEXT,
                    created_at TEXT,
                    resolution_time_hours REAL
                )
            """)
            conn.commit()
