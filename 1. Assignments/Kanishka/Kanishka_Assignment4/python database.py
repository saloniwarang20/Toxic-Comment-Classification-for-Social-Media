
import sqlite3

# Connect to the SQLite database (it will create the file if it doesn’t exist)
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create a 'tasks' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    status INTEGER NOT NULL
)
''')

conn.commit()  # Save changes
conn.close()   # Close the database connection
