# Import the necessary libraries
from flask import Flask, jsonify, request, abort, render_template
from travelDAO import travelDAO  # DAO: handles database operations for trips
from flask_cors import CORS  # Enables CORS for cross-origin requests

# Initialize the Flask app
app = Flask(__name__, template_folder='.')  # HTML templates are in the current directory
CORS(app)  # Enable CORS for all routes

# Route for the home page (renders the HTML interface)
@app.route('/')
def home():
    return render_template("tripviewer.html")

# Route to retrieve all trips from the database
@app.route('/trips')
def get_all_trips():
    trips = travelDAO.getAll()
    return jsonify(trips)

# Route to retrieve a specific trip by its ID
@app.route('/trips/<int:id>')
def get_trip_by_id(id):
    trip = travelDAO.findByID(id)
    return jsonify(trip) if trip else (jsonify({}), 404)  # Return 404 if not found

# Route to create a new trip entry
@app.route('/trips', methods=['POST'])
def create_trip():
    if not request.json:
        abort(400)  # Bad request if no JSON is sent
    trip = {
        "trip_name": request.json['trip_name'],
        "destination": request.json['destination'],
        "start_date": request.json['start_date'],
        "end_date": request.json['end_date'],
        "category_id": request.json['category_id']
    }
    new_trip = travelDAO.create(trip)
    return jsonify(new_trip)

# Route to update an existing trip
@app.route('/trips/<int:id>', methods=['PUT'])
def update_trip(id):
    if not request.json:
        abort(400)
    trip = {
        "trip_name": request.json['trip_name'],
        "destination": request.json['destination'],
        "start_date": request.json['start_date'],
        "end_date": request.json['end_date'],
        "category_id": request.json['category_id']
    }
    travelDAO.update(id, trip)
    trip["id"] = id  # Include the ID in the response
    return jsonify(trip)

# Route to delete a trip by ID
@app.route('/trips/<int:id>', methods=['DELETE'])
def delete_trip(id):
    travelDAO.delete(id)
    return jsonify({"done": True})  # Simple confirmation response

# Run the app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)


