#print sum of number and previuos number
# start  = int(input("Start number: "))
# end  = int(input("End number: "))
# userrange = range(start,end) #create a range staring and ending at user defined values
# for i in userrange:
#     print("Current number is "+str(i)+", previous num is "+str(i-1)+" and sum is "+str(i+i-1))
    # return1

#prints char at even intervals in a string
# text = "The number is , previous num is and sum is "
# for i in text:
#     if text.index(i) % 2 == 0:
#         print(i)
    

#remove first n characters
# msg = input("Text: ")
# toremove = int(input("How many characters to remove from the begining: "))
# result = msg[toremove:]
# print(result)

#check if the first and last number in a list are the same
# mylist = [30,10,20,20,30,40,50,60,10,30]
# first = mylist[0]
# last = mylist[-1]
# if first  == last:
#     mycheck = True
# else:
#     mycheck = False

# print(mycheck)


#numbers from a list divisble by 5 only
# mylist = list(range(0,50))
# for i in mylist:
#     if i%5 == 0 and i != 0:
#         print(i)

#count how many 4 letter sub strings appear in a string

# text = """Video pro buttons that show up where you need them.
#     To change the way a pic ture fits in your document, click it. To change 
#     click Online Video, you can paste in the embed code foru want from the different galleries. Themes and 
#     styles also help keep your document coor dina ted. When you click Design and choose a new Theme, the 
# """
# words_in_text = text.split()
# word_count = 0
# for i in words_in_text:
#     word_length = len(i)
#     if word_length == 4:
#         word_count += 1

# print(word_count)
# print(words_in_text.count("change")) #to count specific word

#CHECKING A PALINDROME
user_input = input("Enter a number: ")
num_length = len(user_input)
firstindex = 0
lastindex = -1
palindromeCheck = True

while  firstindex < int(num_length/2):
    rightchars = user_input[firstindex]
    leftchars = user_input[lastindex]
    if rightchars != leftchars:
        palindromeCheck = False
    firstindex += 1
    lastindex -= 1

if palindromeCheck:
    print("That is a palindrome!")
else:
    print("That's not a palindrome!")

# if num_length % 2 != 0:
#     print("Mid number is "+str(user_input[firstindex]))
# else:
#     print("No mid numnber")