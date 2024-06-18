# Write a decorator hat measurs time thime of function to execute
# import time


# def timer(func):
#     def wrapper(*args):
#         start=time.time()
#         result=func(*args)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start}")
#         return result
#     return wrapper
# @timer
# def example_function(n):
#     time.sleep(n)
# example_function(2)

# Write a decorator whch print func name and the value of its arguments when it is called

def name(func):
    def wrapper(*args):
        result=func(*args)
        print(f"{func.__name__} function has arguments {args}")
        return result
    return wrapper
@name
def add(a,b):
    return a+b
add(1,2)