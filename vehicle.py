print("1.Bike")
print("2.Car")
choice=int(input("Enter your choice here:"))
if choice==1:
    print("What bike?")
    print("1.Scooty")
    print("2.Scooter")
    choice2=int(input("Enter choice2 here:"))
    if choice2==1:
        print("You have selected Scooty")
    elif choice2==2:
        print("You have selected Scooter")
    else:
        print("Wrong choice")
elif choice==2:
    print("What car?")
    print("1.Honda")
    print("2.SUV")
    print("3.Lamborghini")
    choice3=int(input("Enter choice3 here:"))
    if choice3==1:
        print("You have selected Honda")
    elif choice3==2:
        print("You have seleecteed SUV")
    elif choice3==3:
        print("You have selected Lamborghini")
    else:
        print("Wrong choice")

else:
    print("Wrong choice!")





