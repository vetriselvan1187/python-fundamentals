

# simple inheritance example

class Vehicle(ABC):
    def __init__(self, name, vehicle_type, cost):
        self.name = name
        self.vehicle_type = vehicle_type
        self.cost = cost
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def run(self):
        pass


# abstract methods
class PetrolVehicle(Vehicle):
    def __init__(self, name, vehicle_type, cost):
        super().__init__(name, vehicle_type, cost)
    @abstractmethod
    def fill_fuel(self):
        pass

class ElectricVehicle(Vehicle):
    def __init__(self, name, vehicle_type, cost):
         super().__init__(name, vehicle_type, cost)
    @abstractmethod
    def charge(self):
        pass

class Car(PetrolVehicle):
    def __init__(self, name, vehicle_type, cost):
        super().__init__(name, vehicle_type, cost)
        self.num_of_tyres = 4
        self.fuel_capacity = 20
        self.current_fuel_capacity = 0
    def fill_fuel(self, fuel_in_litres):
        self.current_fuel_capacity += fuel_in_litres
    def start(self):
        print(self.name,' is started')
    def stop(self):
        print(self.name,' is stopped')
    def run(self):
        print(self.name, ' is running')
        # while running decrement fuel
    def __repr__(self):
        return '{self.name}-{self.vehicle_type}-{self.cost}-{self.num_of_tyres}'.format(self=self)

class MotorCycle(PetrolVehicle):
    def __init__(self, name, vehicle_type, cost):
        super().__init__(name, vehicle_type, cost)
        self.num_of_tyres = 2
        self.fuel_capacity = 5
        self.current_fuel_capacity = 0
    def start(self):
        print(self.name, ' is started')
    def stop(self):
        print(self.name, ' is stopped')
    def run(self):
        print(self.name, ' is running')
    def __repr__(self):
        return '{self.name}-{self.vehicle_type}-{self.cost}-{self.num_of_tyres}'.format(self=self)



