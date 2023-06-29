# Абстрактные классы для создания продуктов
class Car:
    def drive(self):
        pass

    def stop(self):
        pass


class Motorcycle:
    def ride(self):
        pass

    def brake(self):
        pass


# Конкретные классы продуктов
class SedanCar(Car):
    def drive(self):
        return "Driving Sedan Car"

    def stop(self):
        return "Stopping Sedan Car"


class SportMotorcycle(Motorcycle):
    def ride(self):
        return "Riding Sport Motorcycle"

    def brake(self):
        return "Braking Sport Motorcycle"
    
class SUVCar(Car):
    def drive(self):
        return "Driving SUV Car"

    def stop(self):
        return "Stopping SUV Car"


class StreetMotorcycle(Motorcycle):
    def ride(self):
        return "Riding Street Motorcycle"

    def brake(self):
        return "Braking Street Motorcycle"


# Абстрактная фабрика
class VehicleFactory:
    def create_car(self):
        pass

    def create_motorcycle(self):
        pass


# Конкретная фабрика для создания автомобилей и мотоциклов
class CarMotorcycleFactory(VehicleFactory):
    def create_car(self):
        return SedanCar()

    def create_motorcycle(self):
        return SportMotorcycle()


# Конкретная фабрика для создания других автомобилей и мотоциклов
class SUVStreetMotorcycleFactory(VehicleFactory):
    def create_car(self):
        return SUVCar()

    def create_motorcycle(self):
        return StreetMotorcycle()


# Клиентский код
def main():
    car_motorcycle_factory = CarMotorcycleFactory()
    car = car_motorcycle_factory.create_car()
    motorcycle = car_motorcycle_factory.create_motorcycle()

    print(car.drive())
    print(car.stop())

    print(motorcycle.ride())
    print(motorcycle.brake())


if __name__ == '__main__':
    main()
