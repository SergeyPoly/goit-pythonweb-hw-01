from utils.logger import setup_logger
from factories.us_factory import USVehicleFactory
from factories.eu_factory import EUVehicleFactory
from factories.base_factory import VehicleFactory


def main() -> None:
    setup_logger()

    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    car_us = us_factory.create_car("Ford", "Mustang")
    moto_us = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    car_eu = eu_factory.create_car("Volkswagen", "Golf")
    moto_eu = eu_factory.create_motorcycle("BMW", "R1250GS")

    car_us.start_engine()
    moto_us.start_engine()
    car_eu.start_engine()
    moto_eu.start_engine()


if __name__ == "__main__":
    main()
