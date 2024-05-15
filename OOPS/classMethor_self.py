class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        # self here uses to make the context,in JS it is known as this
        return f"{self.brand} is belong to {self.model}"
my_car=Car("Tata","Nexon")
print(my_car.model)
print(my_car.brand)
print(my_car.full_name())

