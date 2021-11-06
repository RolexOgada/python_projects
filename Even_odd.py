def even_odd(a):
    if(a%2==0):
        return 1
    else:
        return -1
a=int (input("ENTER THE NUMBER: "))

number=even_odd(a)
if(number==1):
    print("Number is Even")
if(number==-1):
    print("Number is Odd")    
    
    

    