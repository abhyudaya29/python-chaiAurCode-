username="chaiAurCode"
x=99

def test():
    # username="chai"
    print(username)
def func2(y=10):
    # Here X will be replaced by Global Variable
    z=x+y
    return z
result=func2(1)
print(result)

# print(username)
# # Here in test the func looks for the global var
# test() 


# in python : is the scope
def func3():
    global x
    x=12
# Over Riding The global Variable
# Bad Practice
func3()
print(x)

def f1():
    x=88
    def f2():
        print(x)
    return f2
# This Is Clousre in python, Here we send the defination and the memory access in f1 as f2
myResult=f1()
myResult()
# Clousre are knows as factory function in Python
def chaiCoder(num):
    def actual(x):
        return x **num
    return actual
f=chaiCoder(2)
g=chaiCoder(3)
print(f(2),">f")
print(g(2),">g")