# travelDAO.py
# This file defines a DAO (Data Access Object) class for managing trip records in a MySQL database.
# It supports basic CRUD operations: Create, Read, Update, Delete.

import mysql.connector  # MySQL connector library
import dbconfig as cfg  # Database config with credentials

class TravelDAO:
    # Initialize database credentials from config
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    # Create and return a new DB cursor
    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # Close DB connection and cursor
    def close_all(self):
        self.cursor.close()
        self.connection.close()

    # Return all trips from DB
    def getAll(self):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM trips")
        results = cursor.fetchall()
        trips = [self.convert_to_dict(row) for row in results]
        self.close_all()
        return trips

    # Return a single trip by ID
    def findByID(self, id):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM trips WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.close_all()
        return self.convert_to_dict(result) if result else None

    # Insert a new trip
    def create(self, trip):
        cursor = self.get_cursor()
        sql = "INSERT INTO trips (trip_name, destination, start_date, end_date, category_id) VALUES (%s, %s, %s, %s, %s)"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"], trip["category_id"])
        cursor.execute(sql, values)
        self.connection.commit()
        trip["id"] = cursor.lastrowid
        self.close_all()
        return trip

    # Update a trip by ID
    def update(self, id, trip):
        cursor = self.get_cursor()
        sql = "UPDATE trips SET trip_name = %s, destination = %s, start_date = %s, end_date = %s, category_id = %s WHERE id = %s"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"], trip["category_id"], id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()

    # Delete a trip by ID
    def delete(self, id):
        cursor = self.get_cursor()
        cursor.execute("DELETE FROM trips WHERE id = %s", (id,))
        self.connection.commit()
        self.close_all()

    # Convert DB row to dictionary
    def convert_to_dict(self, row):
        keys = ["id", "trip_name", "destination", "start_date", "end_date", "category_id"]
        return {keys[i]: row[i] for i in range(len(keys))}

# DAO instance to be used in other files
travelDAO = TravelDAO()
