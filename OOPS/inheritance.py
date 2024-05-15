class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        # self here uses to make the context,in JS it is known as this
        return f"{self.brand} is belong to {self.model}"
class ElectircCar(Car):
    def __init__(self,brand,model,batterySize):
        # self.brand=brand -->This can be done but result in code repetion as this is done on parent class
        super().__init__(brand,model)
        # Super refers to the class which has INIT Method
        self.batterySize=batterySize
    def horn(self):
        print("Pom-Pom")
    

# my_car=Car("Tata","Nexon")
# print(my_car.model)
# print(my_car.brand)
# print(my_car.full_name())
my_electric_Car=ElectircCar("Tata","Nexon","2mvh")

print(my_electric_Car.batterySize)
print(my_electric_Car.brand)
print(my_electric_Car.full_name())
