from dataclasses import dataclass
import datetime

@dataclass
# CLASSE CHE RAPPRESENTA UN PILOTA
class Driver:

    driverId = int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: datetime.date
    nationality: str
    country: str
    url: str

    # RESTITUISCO IL NOME COMPLETO DEL PILOTA
    def __str__(self):
        return f"{self.forename} {self.surname}"

    # USO L'ID COME IDENTIFICATIVO DEL NODO
    def __hash__(self):
        return hash(self.driverId)






