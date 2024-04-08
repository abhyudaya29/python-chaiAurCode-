n=10
# 1 to 10->> sum of even numbers
sum=0
for i in range(1,n+1):
    # range run throuh n-1 so if we want to run till 10 we had done n+1
    if(i%2==0):
        sum=sum+i
        i=i+1
print(sum,">>sum of n even numbers")
    