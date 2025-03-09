from vehicle_factory import VehicleFactory


if __name__ == "__main__":
    sedan = VehicleFactory.create_vehicle("seDan")
    print(sedan.create_vehicle("Porsche", 2018))
