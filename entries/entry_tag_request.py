import sqlite3
import json
from models import Tag
      

def get_entries_with_tags(entry_id):
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()     
        
        db_cursor.execute("""
            SELECT 
                t.id,
                t.name tag_name
            FROM Tags t
            JOIN entry_tag e
                ON t.id = e.tag_id
            WHERE e.entry_id = ?
            """, (entry_id,))
                
        tag_entry= db_cursor.fetchall()

        tags = []

        for row in tag_entry:
            tag = Tag(row['id'], row['tag_name'])

            tags.append(tag.__dict__)

        return tags