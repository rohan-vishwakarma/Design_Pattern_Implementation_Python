from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    This is abstract class for All The Vehicle Types
    """
    @abstractmethod
    def create_vehicle(self):
        pass
