my_str = input("Enter a string : ")

# breakdown the string into list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words
for w in words:
    print(w, end= " ")