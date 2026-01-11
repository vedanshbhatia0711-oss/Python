n=int(input("Enter n here:"))
print("numbers from {0} to {1} are:".format(n,1))
sum=0
for i in range(n,0,-2):
    sum=sum+i
print("sum=",sum)