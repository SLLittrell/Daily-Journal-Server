import sqlite3
import json
from models import moods


def get_all_moods():
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        """)

        moods = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    return json.dumps(moods)

# Function with a single parameter
def get_single_mood(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        WHERE m.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()

         mood = Mood(data['id'], data['label'])

        return json.dumps(mood.__dict__)

# def get_entry_by_search(search_term):
#     with sqlite3.connect("./dailyjournal.db") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#          SELECT
#             m.id,
#             m.label
#         FROM moods m
#         WHERE m.concept LIKE ?
#         """, ( f"%{search_term}%", ))
        
        
#         moods = []

#         dataset = db_cursor.fetchall()

#         for row in dataset:

#             entry = moods(row['id'], row['date'], row['concept'], row['entry'], row['moodId'], row['instructorId'])

#             moods.append(entry.__dict__)

#     return json.dumps(moods)


# def create_entry(entry):
#     max_id = EMPLOYEES[-1]["id"]
  
#     new_id = max_id + 1
  
#     employee["id"] = new_id
  
#     EMPLOYEES.append(employee)

#     return employee
def delete_mood(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM moods
        WHERE id = ?
        """, (id, ))
