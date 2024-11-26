from flask import Flask, render_template, request, redirect
from create_db import init_db 
import sqlite3

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        description = request.form['description']
        status = request.form.get('status', 0)
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (description, status) VALUES (?, ?)', (description, status))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        description = request.form['description']
        status = request.form.get('status', 0)
        cursor.execute('UPDATE tasks SET description = ?, status = ? WHERE id = ?', (description, status, id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
    task = cursor.fetchone()
    conn.close()
    return render_template('update.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

