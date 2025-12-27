Amount=int(input("Enter money value here:"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("number of note_1=", note_1)
print("number of note_2=", note_2)
print("number of note_3=", note_3)