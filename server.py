from flask import Flask, jsonify, request, abort, render_template
from travelDAO import travelDAO
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

@app.route('/')
def home():
    return render_template("tripviewer.html")

@app.route('/trips')
def getAll():
    results = travelDAO.getAll()
    return jsonify(results)

@app.route('/trips/<int:id>')
def findById(id):
    trip = travelDAO.findByID(id)
    return jsonify(trip) if trip else (jsonify({}), 404)

@app.route('/trips', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    trip = {
        "trip_name": request.json['trip_name'],
        "destination": request.json['destination'],
        "start_date": request.json['start_date'],
        "end_date": request.json['end_date'],
    }
    new_trip = travelDAO.create(trip)
    return jsonify(new_trip)

@app.route('/trips/<int:id>', methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    trip = {
        "trip_name": request.json['trip_name'],
        "destination": request.json['destination'],
        "start_date": request.json['start_date'],
        "end_date": request.json['end_date'],
    }
    travelDAO.update(id, trip)
    trip["id"] = id
    return jsonify(trip)

@app.route('/trips/<int:id>', methods=['DELETE'])
def delete(id):
    travelDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)

