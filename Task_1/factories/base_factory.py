from typing import Protocol
from models.car import Car
from models.motorcycle import Motorcycle


class VehicleFactory(Protocol):
    def create_car(self, make: str, model: str) -> Car: ...

    def create_motorcycle(self, make: str, model: str) -> Motorcycle: ...
