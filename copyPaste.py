import pyperclip
text = pyperclip.paste() #pasting the content of copied text
print(text)

name = input("Enter your name ")
age = input("Enter your age ")
you = "my name is "+name+" and am "+age+" years old"
pyperclip.copy(you) #copying the content of variable you