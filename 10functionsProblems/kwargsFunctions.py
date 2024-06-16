def printKwargs(**kwargs):
    # print(**kwargs)
    for key,value in kwargs.items():
        print(f"{key} {value}")

    
   


printKwargs(name="Abhyudaya",power="Lazer")