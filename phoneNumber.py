# kenyan phone number format is +254 712 345678
def isPhoneNumber(text):
    if len(text) != 15:
        return False #not phone number sized
    if text[0] != "+":
        return False #begining char is not +
    
    for i in range(1,4):
        if not text[i].isdecimal():
            return False #no area code
        
    if text[4] != " ":
        return False #missing dash
    
    for i in range(5,8):
        if not text[i].isdecimal():
            return False #no first 3 digits
        
    if text[8] != " ":
        return False #missing second dash
    
    for i in range(9,14):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True
# print(isPhoneNumber('123-234-5554'))