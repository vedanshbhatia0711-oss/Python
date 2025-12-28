actualcost=float(input("Enter cost here:"))
Sale_amount=float(input("Enter sales amount here:"))
if Sale_amount > actualcost:
    amount=Sale_amount-actualcost
    print("Total profit={0}" .format(amount))
else:
    print("Loss!")



