import pyperclip,re
import os

phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
email_regex = re.compile(r"[a-zA-Z0-9_+.]+@[a-zA-Z09_+.]+")
text = pyperclip.paste()
matched_phone = phone_regex.findall(text)
matched_email = email_regex.findall(text)

for i in matched_email:
    print(i)
for i in matched_phone:
    print(i)

# print("\\")
# print(r"\\")