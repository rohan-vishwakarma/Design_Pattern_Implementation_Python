from vehicle_type import Sedan, Suv, Bus, VehicleTypeEnum

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str):
        vehicle_type = vehicle_type.lower()
        if vehicle_type == VehicleTypeEnum.SEDAN.name.lower():
            return Sedan()
        elif vehicle_type == VehicleTypeEnum.SUV.name.lower():
            return Suv()
        elif vehicle_type == VehicleTypeEnum.BUS.name.lower():
            return Bus()
        else:
            raise ValueError("Invalid Vehicle Type")
