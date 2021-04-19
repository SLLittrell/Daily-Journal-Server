import sqlite3
import json
from models import Entries
from models import Mood
from models import Instructor
from models import Tag


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
            
        
        db_cursor.execute("""
        SELECT 
            t.name tag_name
        FROM Tags t
        JOIN entry_tag
            ON t.id = entry_tag.tag_id
        WHERE entry_id = ?
        """, (row['id'],))
            
    
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

        for tag in new_entry["tags"]:
            db_cursor.execute("""
            INSERT INTO entry_tag 
                (entry_id, tag_id)
            VALUES (?,?)""",(id, tag))

    return json.dumps(new_entry)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))


def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Entries
                SET
                    id = ?,
                    date = ?,
                    concept = ?,
                    entry = ?,
                    moodId = ?,
                    instructorId = ?
            WHERE id = ?
        """, (new_entry['id'], new_entry['date'], new_entry['concept'],
              new_entry['entry'], new_entry['moodId'],
              new_entry['instructorId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True