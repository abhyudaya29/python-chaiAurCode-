def sumOfMultipleSu(*args):
    print(*args,">>>The arguments we passed")
    sum=0
    for values in args:
        print("vaues are: ",values,"args are: ",args)
        sum=sum+values
    return sum
print(sumOfMultipleSu(1,2,3))