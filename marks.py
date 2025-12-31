print("Enter Marks Obtained in 5 subjects")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
average=total/5
if average>81 and average<=91:
    print("Your mark is A1")
elif average>71 and average<=80:
    print("Your mark is A2")
elif average>61 and average<=70:
    print("Your mark is B1")
elif average>55 and average<=60:
    print("Your mark is B2")
elif average>50 and average<=55:
    print("Your mark is C")
else: 
    print("Invalid input")
