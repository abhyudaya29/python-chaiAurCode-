import time

def timer(func):
    def wrapper(*args,**kwargs):
        starttime=time.time()
        result=func(*args,**kwargs)
        endTime=time.time()
        print(f"{func.__name__} run in  {endTime-starttime}")
        return result
    return wrapper
# decorator is like toll-booth
@timer
def example_func(n):
    time.sleep(n)
example_func(2)