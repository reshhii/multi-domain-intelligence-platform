from db.database import get_connection

def create_incident(severity, status, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cyber_incidents (severity, status, category) VALUES (?, ?, ?)",
        (severity, status, category)
    )
    conn.commit()
    conn.close()

def get_all_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cyber_incidents")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_incident_by_id(incident_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM cyber_incidents WHERE id = ?",
        (incident_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def update_incident_status(incident_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cyber_incidents SET status = ? WHERE id = ?",
        (new_status, incident_id)
    )
    conn.commit()
    conn.close()

def delete_incident(incident_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM cyber_incidents WHERE id = ?",
        (incident_id,)
    )
    conn.commit()
    conn.close()
