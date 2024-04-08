ip_str="teeteraabbcd"

for i in ip_str:
    print(i)
    if(ip_str.count(i)==1):
        print("char is: ",i)
        break

