def add(num1,num2):
    if(isinstance(num1,(int,float))and isinstance(num2,(int,float))):
        # isinstance is used to check the type of the object, its is str or int or float
        return num1+num2
    else:
        raise TypeError("Numbers cant be string")
print(add("a","b"))