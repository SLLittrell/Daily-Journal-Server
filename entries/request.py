import sqlite3
import json
from models import Entries


def get_all_entries():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            moodId,
            instructorId
        FROM entries e
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entries = Entries(row['id'], row['date'], row['concept'], row['entry'], row['moodId'], row['instructorId'])

            entries.append(entries.__dict__)

    return json.dumps(entries)

# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            moodId,
            instructorId
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()

        entry = Entries(data['id'], data['name'], data['location_id'])

        return json.dumps(entry.__dict__)


# def create_entry(entry):
#     max_id = EMPLOYEES[-1]["id"]
  
#     new_id = max_id + 1
  
#     employee["id"] = new_id
  
#     EMPLOYEES.append(employee)

#     return employee

# def delete_employee(id):
#     employee_index = -1
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             employee_index = index

#     if employee_index >= 0:
#         EMPLOYEES.pop(employee_index)

# def update_employee(id, new_employee):
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             EMPLOYEES[index] = new_employee
#             break