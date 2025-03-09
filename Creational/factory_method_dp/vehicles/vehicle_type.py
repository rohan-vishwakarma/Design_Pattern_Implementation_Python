from enum import Enum
from vehicle import Vehicle

class VehicleTypeEnum(Enum):
    SUV   = "SUV"
    SEDAN = "SEDAN"
    BUS   = "BUS"

class Suv(Vehicle):
    def create_vehicle(self):
        return "Creating Suv Vehicle Type"

class Sedan(Vehicle):
    def create_vehicle(self, vehicle_name: str, model: str):
        return {
            "vehicle_name" : vehicle_name,
            "model" : model
        }

class Bus(Vehicle):
    def create_vehicle(self):
        return "Creating Bus Vehicle"



