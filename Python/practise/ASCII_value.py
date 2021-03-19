
c= input("Enter a character (not string) : ")

char=c.split()
for i in char:
    if (len(i)>1):
        print("More than one character found! Please input a single character")
    else:
        print("The ASCII value of", c, "is",ord(i))

print()