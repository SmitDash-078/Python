"""
Mad libs generator
_______________________________
"""

# Loop back to this point once the codde finishes
loop=1
while(loop<10):

    # All the questions that the program asks the user

    noun = input("Choose a noun : ")
    p_noun = input("Choose a plural noun : ")
    noun2 = input("Choose a noun : ")
    place = input("Choose a place : ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun : ")

    # Displays the story based on the users input

    print("___________________________________")
    print("Be kind to your",noun,"-footed",p_noun)
    print("For a duck may be somebody's", noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is this the", noun3,",")
    print("Well it is.")
    print("____________________________________")

    # Loop back to "loop = 1"
    loop=loop+1
