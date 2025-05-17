from flask import Flask, request, render_template, redirect, url_for, abort
from datetime import datetime
import json
import os

app = Flask(__name__, static_url_path='/static')

DATA_FILE = os.path.join(app.root_path, 'storage', 'data.json')

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка з формою
@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        data = request.form
        new_message = {
            "username": data.get("username", "Anonymous"),
            "message": data.get("message", "")
        }
        try:
            with open(DATA_FILE, 'r') as f:
                messages = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            messages = {}

        messages[str(datetime.now())] = new_message

        with open(DATA_FILE, 'w') as f:
            json.dump(messages, f, indent=4)

        return redirect(url_for('index'))
    return render_template('message.html')

# Виведення збережених повідомлень
@app.route('/read')
def read():
    try:
        with open(DATA_FILE, 'r') as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = {}
    return render_template('read.html', messages=messages)

# Обробка помилки 404
@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)
