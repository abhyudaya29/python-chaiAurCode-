class Car:
    total_car=0
    # __init__ is a constructor which takes the parameter
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
       Car.total_car+=1
    def fuel_type(self):
        return "PEtrol or Desiel"
    @staticmethod
    # by static method the access get only to class ,not to the objects
    def general_defination():
        return "Cars are means of Transport"



class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize=batterysize
    def fuel_type(self):
        return "Electric charge"
my_car=ElectricCar("Tesla","R18","2mvh")
my_old_car=Car("Tata","Safari")
my_new_car=Car("Tata","Safari")
# print(my_car.fuel_type())
# print(my_old_car.fuel_type())
# print(my_old_car.general_defination())
print(Car.general_defination())
print(Car.total_car)

