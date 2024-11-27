
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def home():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('home.html', tasks=tasks)
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        description = request.form['description']
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (description, status) VALUES (?, ?)',
                     (description, 0))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('create.html')
@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        description = request.form['description']
        status = request.form.get('status') == 'on'
        conn.execute('UPDATE tasks SET description = ?, status = ? WHERE id = ?',
                     (description, int(status), id))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('update.html', task=task)
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
import webbrowser

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")  # This opens the URL in your default browser
    app.run(debug=True)
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
