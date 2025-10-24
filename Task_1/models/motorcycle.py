import logging
from .vehicle import Vehicle


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")
