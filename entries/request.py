import sqlite3
import json
from models import Entries
from models import Mood
from models import Instructor


def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.moodId,
            e.instructorId,
            m.label,
            i.first_name
        FROM entries e
        JOIN Moods m
            ON m.id = e.moodId
        JOIN Instructors i
            ON i.id = e.instructorId
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entries(row['id'], row['date'], row['concept'], row['entry'], row['moodId'], row['instructorId'])

            mood = Mood(row['moodId'], row['label'])

            instructor = Instructor(row['instructorId'], row['first_name'])
            
            entry.mood = mood.__dict__

            entry.instructor = instructor.__dict__
            
            entries.append(entry.__dict__)

    return json.dumps(entries)

# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.moodId,
            e.instructorId
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()

        entry = Entries(data['id'], data['date'], data['concept'], data['entry'], data['moodId'], data['instructorId'])

        return json.dumps(entry.__dict__)

def get_entry_by_search(search_term):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.moodId,
            e.instructorId
        FROM entries e
        WHERE e.concept LIKE ?
        """, ( f"%{search_term}%", ))
        
        
        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entries(row['id'], row['date'], row['concept'], row['entry'], row['moodId'], row['instructorId'])

            entries.append(entry.__dict__)

    return json.dumps(entries)


def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            ( date, concept, entry, moodId, instructorId )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_entry['date'], new_entry['concept'],
              new_entry['entry'], new_entry['moodId'],
              new_entry['instructorId'], ))
       
        id = db_cursor.lastrowid
       
        new_entry['id'] = id


    return json.dumps(new_entry)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))



# def update_employee(id, new_employee):
#     for index, employee in enumerate(EMPLOYEES):
#         if employee["id"] == id:
#             EMPLOYEES[index] = new_employee
#             break