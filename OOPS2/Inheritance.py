class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        # __brand means that we have made the brand private
        self.model=model
    def get_brand(self):
        # making a getter method 
        return self.__brand +"!"

    def full_name(self):
        return f"{self.__brand} has car {self.model}"

class ElectricCar(Car):
    def __init__(self,battery,brand,model):
        self.battery=battery
        # super() method refer to init of its Parent class
        super().__init__(brand,model)

my_car=Car("Mahindra","Thar")
# print(my_car.brand)
# print(my_car.full_name())
my_electric_car=ElectricCar("35kwh","Tesla","Model S")
# print(my_electric_car.brand)
print(my_electric_car.get_brand())
print(my_electric_car.full_name())