import logging
from .vehicle import Vehicle


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")
