from flask import Flask, request, jsonify, render_template
import sqlite3

#Flask: The main web framework you're using.
#request: Lets you access data sent from the frontend (like form data).
#jsonify: Converts Python data to JSON to send to the frontend.
#render_template: Renders HTML files.
#sqlite3: Built-in Python module to use a SQLite database.

#creates your Flask app
app = Flask(__name__)

# database creation
#Connects to the SQLite database file travel.db.
#Creates a table called trips if it doesn't already exist.
#Each trip has an ID, name, destination, start date, and end date

def init_db():
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trip_name TEXT NOT NULL,
            destination TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Main route
@app.route('/')
def index():
    return render_template('index.html')

# API: Get all trips
@app.route('/api/trips', methods=['GET'])
def get_trips():
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trips')
    trips = cursor.fetchall()
    conn.close()
    return jsonify(trips)

# API: Add a new trip
@app.route('/api/trips', methods=['POST'])
def add_trip():
    data = request.get_json()
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trips (trip_name, destination, start_date, end_date) VALUES (?, ?, ?, ?)',
                   (data['trip_name'], data['destination'], data['start_date'], data['end_date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Viagem adicionada com sucesso'})

# Run the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

