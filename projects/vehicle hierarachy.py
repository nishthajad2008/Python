class Vehicle():
    def __init__(self,brand: str, speed: int):
        self.brand = brand
        self.speed = speed
    def drive(self):
        return f"{self.brand} is driving at {self.speed} mph."
class Car(Vehicle):
    def __init__(self,brand: str, speed:int,num_door: int):
        super().__init__(brand , speed)
        self.num_door = num_door
    def drive(self):
        return f"{self.brand} car with {self.num_doors} doors is cruising at {self.speed} mph."
class ElectricCar(Car):
    def __init__(self, brand: str, speed: int, num_door: int, battery_level: int):
        super().__init__(brand,speed,num_door)
        self.battery_level = battery_level
    def charge(self):
        self.battery_level = 100
        return "Fully charged!"