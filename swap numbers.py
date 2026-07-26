char = input("enter a character: ")

if len(char) == 1:
    print("ASCII value of", char, "is", ord(char))
else:
    print("Please only one character.")