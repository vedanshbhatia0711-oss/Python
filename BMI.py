height=float(input("Enter height in cm here:"))
weight=float(input("Enter weight in kg here:"))
BMI=weight/(height/100)**2
if BMI <= 18.4:
    print("You are underweight")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <= 40:
    print("You are overweight")
elif BMI <= 55:
    print("You are severely overweight")
elif BMI <= 60:
    print("You are obese")
else: 
    print("You are severely obese")