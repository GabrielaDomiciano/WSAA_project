# travelDAO.py
# MySQL data access layer for trips (following professor's DAO style)

import mysql.connector
import dbconfig as cfg

class TravelDAO:
    connection = ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM trips")
        results = cursor.fetchall()
        trips = []
        for row in results:
            trips.append(self.convert_to_dict(row))
        self.close_all()
        return trips

    def findByID(self, id):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM trips WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.close_all()
        return self.convert_to_dict(result) if result else None

    def create(self, trip):
        cursor = self.get_cursor()
        sql = "INSERT INTO trips (trip_name, destination, start_date, end_date) VALUES (%s, %s, %s, %s)"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"])
        cursor.execute(sql, values)
        self.connection.commit()
        trip["id"] = cursor.lastrowid
        self.close_all()
        return trip

    def update(self, id, trip):
        cursor = self.get_cursor()
        sql = "UPDATE trips SET trip_name = %s, destination = %s, start_date = %s, end_date = %s WHERE id = %s"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"], id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()

    def delete(self, id):
        cursor = self.get_cursor()
        cursor.execute("DELETE FROM trips WHERE id = %s", (id,))
        self.connection.commit()
        self.close_all()

    def convert_to_dict(self, row):
        keys = ["id", "trip_name", "destination", "start_date", "end_date"]
        return {keys[i]: row[i] for i in range(len(keys))}

# Create DAO instance to be imported in server.py
travelDAO = TravelDAO()


