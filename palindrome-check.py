#CHECKING A PALINDROME
#a number that if reversed remains the same e.g mum

user_input = input("\nEnter a text or number: ")
num_length = len(user_input)
firstindex = 0
lastindex = -1
palindromeCheck = True

while  firstindex < num_length/2:
    rightchars = user_input[firstindex]
    leftchars = user_input[lastindex]

    if rightchars != leftchars:
        palindromeCheck = False

    firstindex += 1
    lastindex -= 1

if palindromeCheck:
    print("That is a palindrome!\n")
else:
    print("That's not a palindrome!\n")