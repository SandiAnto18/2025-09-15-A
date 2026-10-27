from dataclasses import dataclass
import datetime

@dataclass
class Driver:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: datetime.date
    nationality: str
    url: str




    def __hash__(self):
        return hash(self.driverId)

    def __str__(self):
        return f"{self.driverRef} ({self.forename}, {self.surname})"