import os
import time
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'flaskuser')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'flask_db')

# Initialize MySQL
mysql = MySQL(app)

# new code to handle DB connection retries

def init_db():
    with app.app_context():
        for i in range(5):  # retry 5 times
            try:
                cur = mysql.connection.cursor()
                cur.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    message TEXT
                );
                ''')
                mysql.connection.commit()
                cur.close()
                print("DB connected successfully")
                break
            except Exception as e:
                print("DB not ready, retrying...", e)
                time.sleep(5)

# def init_db():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         cur.execute('''
#         CREATE TABLE IF NOT EXISTS messages (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             message TEXT
#         );
#         ''')
#         mysql.connection.commit()  
#         cur.close()

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': new_message})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)