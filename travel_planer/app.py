from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Criação automática do banco de dados
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

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# API: obter todas as viagens
@app.route('/api/trips', methods=['GET'])
def get_trips():
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trips')
    trips = cursor.fetchall()
    conn.close()
    return jsonify(trips)

# API: adicionar uma nova viagem
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

# Executa o app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

