#CHECKING A PALINDROME
#a number that if reversed remains the same e.g mum

def userinput(text):
    num_length = len(text)
    lastindex = -1
    reversedText = ""

    while num_length !=0:
        reversedText = reversedText + text[lastindex]
        num_length -= 1
        lastindex -= 1

    if reversedText == text:
        print("That is a palindrome!\n")
    else:
        print("That's not a palindrome!\n")



user_input = input("\nEnter a text or number: ")
userinput(user_input)