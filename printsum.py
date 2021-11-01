#print sum of number and previuos number
# start  = int(input("Start number: "))
# end  = int(input("End number: "))
# userrange = range(start,end)
# for i in userrange:
#     print("The number is "+str(i)+", previous num is "+str(i-1)+" and sum is "+str(i+i-1))
    # return1

#prints char at even intervals in a string
# text = "The number is , previous num is and sum is "
# for i in text:
#     if text.index(i) % 2 == 0:
#         print(i)
    

#remove first n characters
msg = input("Text: ")
toremove = int(input("How many characters to remove from the begining: "))
result = msg[toremove:]
print(result)