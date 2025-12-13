import pandas as pd
import sqlite3

DB_PATH = "db/platform.db"
CSV_PATH = "data/cyber_incidents.csv"

def load_csv_to_db():
    df = pd.read_csv(CSV_PATH)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("cyber_incidents", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    load_csv_to_db()
