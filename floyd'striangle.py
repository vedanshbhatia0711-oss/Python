rows=int(input("Enter number of rows here:"))
number=1
print("Floyd's triangle")
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print(number, end="")
        number=number+1
    print()