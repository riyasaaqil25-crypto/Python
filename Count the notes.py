amount =int(input("please enter amount for withdrawl:"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("notes of 100 pounds" , note_1)
print("notes of 50 pounds" , note_2)
print("notes of 10 pounds" , note_3)