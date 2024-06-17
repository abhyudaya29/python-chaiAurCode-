class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} has car {self.model}"
    
my_car=Car("Mahindra","Thar")
print(my_car.brand)
print(my_car.full_name())