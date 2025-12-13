import sqlite3

DB_PATH = "db/platform.db"

def incidents_by_severity():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT severity, COUNT(*) AS total
        FROM cyber_incidents
        GROUP BY severity
    """)

    results = cursor.fetchall()
    conn.close()
    return results


def incidents_by_status():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM cyber_incidents
        GROUP BY status
    """)

    results = cursor.fetchall()
    conn.close()
    return results
