# travelDAO.py
# Acesso ao banco MySQL para viagens (estilo do professor)

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

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM trips")
        results = cursor.fetchall()
        trips = []
        for row in results:
            trips.append(self.convertToDictionary(row))
        self.closeAll()
        return trips

    def findByID(self, id):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM trips WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDictionary(result) if result else None

    def create(self, trip):
        cursor = self.getcursor()
        sql = "INSERT INTO trips (trip_name, destination, start_date, end_date) VALUES (%s, %s, %s, %s)"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"])
        cursor.execute(sql, values)
        self.connection.commit()
        trip["id"] = cursor.lastrowid
        self.closeAll()
        return trip

    def update(self, id, trip):
        cursor = self.getcursor()
        sql = "UPDATE trips SET trip_name = %s, destination = %s, start_date = %s, end_date = %s WHERE id = %s"
        values = (trip["trip_name"], trip["destination"], trip["start_date"], trip["end_date"], id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        cursor.execute("DELETE FROM trips WHERE id = %s", (id,))
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, row):
        keys = ["id", "trip_name", "destination", "start_date", "end_date"]
        return {keys[i]: row[i] for i in range(len(keys))}

# Cria o DAO pronto para importar no server.py
travelDAO = TravelDAO()

