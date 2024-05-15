class Car:
    # __init__ is a constructor which takes the parameter
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model



my_car=Car("Toyota","Corollia")
print(my_car.model)
print(my_car.brand)


my_new_car=Car("Tata","Safari")
print(my_new_car.brand)
    
