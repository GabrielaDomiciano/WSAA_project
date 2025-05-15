

from flask import Flask, request, jsonify, abort, render_template
import sqlite3

# Cria o app Flask
app = Flask(__name__)

# Cria o banco de dados automaticamente (se não existir)
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

# Página inicial (opcional - só texto para testes)
@app.route('/')
def index():
    return render_template('index.html')

# Retorna todas as viagens (GET)
@app.route('/trips', methods=['GET'])
def get_all():
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips")
    rows = cursor.fetchall()
    conn.close()

    trips = []
    for row in rows:
        trips.append(convert_to_dict(row))
    return jsonify(trips)

# Retorna uma viagem por ID (GET)
@app.route('/trips/<int:id>', methods=['GET'])
def find_by_id(id):
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify(convert_to_dict(row))
    else:
        return jsonify({}), 404

# Cria uma nova viagem (POST)
@app.route('/trips', methods=['POST'])
def create():
    trip = request.json
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    sql = "INSERT INTO trips (trip_name, destination, start_date, end_date) VALUES (?, ?, ?, ?)"
    values = (trip.get("trip_name"), trip.get("destination"), trip.get("start_date"), trip.get("end_date"))
    cursor.execute(sql, values)
    conn.commit()
    trip["id"] = cursor.lastrowid  # Adiciona o ID criado automaticamente
    conn.close()
    return jsonify(trip)

# Atualiza uma viagem existente (PUT)
@app.route('/trips/<int:id>', methods=['PUT'])
def update(id):
    trip = request.json
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    sql = "UPDATE trips SET trip_name=?, destination=?, start_date=?, end_date=? WHERE id=?"
    values = (trip.get("trip_name"), trip.get("destination"), trip.get("start_date"), trip.get("end_date"), id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    trip["id"] = id  # Garante que o ID seja retornado no JSON
    return jsonify(trip)

# Remove uma viagem (DELETE)
@app.route('/trips/<int:id>', methods=['DELETE'])
def delete(id):
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trips WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"done": True})

# Converte uma linha do banco em dicionário (para o JSON)
def convert_to_dict(row):
    keys = ["id", "trip_name", "destination", "start_date", "end_date"]
    return {keys[i]: row[i] for i in range(len(keys))}

# Inicializa o banco e roda o app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)


