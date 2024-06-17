class Car:
    # __init__ is a constructor 
    def __init__(self,brand,model):
        # Self here define a current context
        # in Js it is fullfilled with JS,In Python we use self
        self.brand=brand
        self.model=model


my_car=Car("Tata","Punch")
print(my_car)
print(my_car.brand)
print(my_car.model)


my_new_car=Car("Mahindra","Scorpio")
print(my_new_car.model)