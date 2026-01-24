num=int(input("Enter number here:"))
count=0
while num!=0:
    num//=10
    count=count+1
print("Number of digits=" + str(count))
