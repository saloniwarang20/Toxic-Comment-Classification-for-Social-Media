from flask import Flask, render_template, request, redirect
import sqlite3
import webbrowser

app = Flask(__name__)

# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row  # To fetch rows as dictionaries
    return conn

# Home route to display tasks
@app.route('/')
def home():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('home.html', tasks=tasks)

# Route to create a new task
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        description = request.form['description']
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (description, status) VALUES (?, ?)',
                     (description, 0))  # Status is 0 for incomplete
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('create.html')

# Route to update an existing task
@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        description = request.form['description']
        status = request.form.get('status') == 'on'  # Checkbox value
        conn.execute('UPDATE tasks SET description = ?, status = ? WHERE id = ?',
                     (description, int(status), id))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('update.html', task=task)

# Route to delete a task
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")  # Opens the URL in the default browser
    app.run(debug=True)
