# admin to create a user account
# use the account to login
# admin user can the add other users or delete them
# users can log in but only view other users without any modification to them

users = {}
def inputPrompt(prompt):
    userInput  = input(prompt+": ")
    return userInput

def createUser():
    username = inputPrompt("Enter your username")
    username = inputPrompt("Enter your password")
# i will complete this later