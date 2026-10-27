
from database.DB_connect import DBConnect
from model.driver import Driver


class DAO:

    @staticmethod
    def getAllYears():
        # RECUPERO TUTTI GLI ANNI DISPONIBILI
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT DISTINCT year
            FROM seasons
            ORDER BY year
        """

        cursor.execute(query)
        results = []

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
       #@staticmethod non richiede self
    def getDriver(da, a):
        # RECUPERO I PILOTI CHE HANNO CONCLUSO ALMENO UNA GARA
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT DISTINCT d.*
            FROM drivers d, results r, races rc
            WHERE d.driverId = r.driverId
              AND r.raceId = rc.raceId
              AND rc.year BETWEEN %s AND %s
              AND r.position IS NOT NULL
        """

        cursor.execute(query, (da, a))
        results = []

        for row in cursor:
            # TRASFORMO OGNI RIGA IN UN OGGETTO DRIVER
            results.append(Driver(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getP1P2peso(da, a):
        # RECUPERO LE COPPIE DI PILOTI E IL PESO DEGLI ARCHI
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT d.driverId AS pilota1,
                   d2.driverId AS pilota2,
                   COUNT(DISTINCT r.raceId) AS peso
            FROM drivers d, results r, races rc,
                 drivers d2, results r2, races rc2
            WHERE d.driverId = r.driverId
              AND r.raceId = rc.raceId
              AND rc.year BETWEEN %s AND %s
              AND r.position IS NOT NULL
              AND d2.driverId = r2.driverId
              AND r2.raceId = rc2.raceId
              AND rc2.year BETWEEN %s AND %s
              AND r2.position IS NOT NULL
              AND r2.raceId = r.raceId
              AND r.constructorId = r2.constructorId 
              AND d.driverId < d2.driverId
            GROUP BY pilota1, pilota2
        """
        #P1 E P2 STESSA GARA -> AND r2.raceId = rc2.raceId
        #P1 E P2 COMPAGNI DI SQUADRA(stesso Id di squadra) -> AND r.constructorId = r2.constructorId

        cursor.execute(query, (da, a, da, a))
        results = []

        for row in cursor:
            # SALVO ID DEI DUE PILOTI E PESO
            results.append((
                row["pilota1"],
                row["pilota2"],
                row["peso"]
            ))

        cursor.close()
        conn.close()
        return results

