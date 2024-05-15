class Car:
    def __init__(self,brand,model):
        # self.brand=brand
        # To make any varibale private, we do __ before the variable like __brand
        # __brand is only accessiable in Class Not in Object
        self.__brand=brand

        self.model=model
    def get_brand(self):
        return self.__brand +"!"
my_car=Car("Tesla","R18")
# print(my_car.__brand)
print(my_car.get_brand())