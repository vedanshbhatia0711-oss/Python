Unit=int(input("Enter number of units here:"))
if Unit<=50:
    amount=Unit*2.60
    surcharge=125
elif Unit<=100:
    amount=135+((Unit-50)*3.50)
    surcharge=135
elif Unit<=200:
    amount=150+((Unit-50)*4.50)
    surcharge=200
else:
    print("Charge is 100000")
Total=amount+surcharge
print("Toatal=", Total)