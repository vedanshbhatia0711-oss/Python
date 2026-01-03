medical_cause=str(input("Did you have medical cause: Y or N:"))
atten=int(input("Enter attendance here:"))
if medical_cause=="Y":
    print("Allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")


