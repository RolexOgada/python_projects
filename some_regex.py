#using a regular expression to find values in a large text
import re
large_text = """my this should be a large text message, i want to find phone numbers  712 195 774 and 
also find batsomething, bakttalion, batwoman, collince
"""

# regex_phone = re.compile(r"\d") #\d numeric digit 0-9, same as below with pipes
# regex_phone = re.compile(r"(0|1|2|3|4|5|6|7|8|9)") 
#******************************************
# \d numeric digit
# \D any non-numeric(0-9) character
# \w any letter,numeric digit or underscore char
# \W any character not letter, numeric digit or underscore
# \s any space,tab or new line character
# \S any character not space,tab, or new line
#******************************************
# custom regex
lowerCaseVowelsRegex = re.compile(r'[aeiou]')
allCaseVowelsRegex = re.compile(r'[aeiouAEIOU]')
allCaseVowelsRegex = re.compile(r'[^aeiouAEIOU]') #returns non vowel in the text
upperCaseRegex = re.compile(r'[A-Z]')
upperCaseRegex = re.compile(r'[A-F]')
upperCaseRegex = re.compile(r'^Hello') #return text when the string strictly begins with Hello
upperCaseRegex = re.compile(r'Hello$') #return text when the string strictly ends with Hello
upperCaseRegex = re.compile(r'^Hello$') #return strictly the word Hello
upperCaseRegex = re.compile(r'.at') #return any word ending with 'at'
upperCaseRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #return all charaters after first name: and all characters after second name:

upperCaseRegex = re.compile(r'^\d+$') #return strictly an all digit number (one or more) e.g 1223 returns 1223 while 12c3 returns none
allCaseRegex = re.compile(r'[a-zA-Z]') #gives caps and lower


textRegex = re.compile(r'\d+\s\w+') #one or more(+) digit, one space\new line\tab, one or more word characters

# regex_phone = re.compile(r"(\d\d\d) (\d\d\d) (\d\d\d \d\d\d)") 
regex_phone = re.compile(r"(\d\d\d)? \d\d\d \d\d\d \d\d\d") #area code can only appear once or zero times...it's optional
regex_phone = re.compile(r"(\d\d\d)* \d\d\d \d\d\d \d\d\d") #area code can appear zero or many times...
regex_phone = re.compile(r"(\d\d\d)+ \d\d\d \d\d\d \d\d\d") #area code can appear one or many times...
regex_phone = re.compile(r"((\d\d\d)? \d\d\d \d\d\d \d\d\d(,)?){3}") #matches area phone numbers that appear 3 times in a row...
#regular expressions do greedy matches, it returns the maximum longest matching pattern
#to do a non-greedy match
regex_phone = re.compile(r"(\d\d){2,5}?") #the question matk enables python to perform non-gready match by matching the smallest possible
regex_phone = re.compile(r"((\d\d\d)? \d\d\d \d\d\d \d\d\d(,)?){3,5}") #matches area phone numbers that appear minimum of 3 times and maximum of 5 times in a row...
regex_phone = re.compile(r"((\d\d\d)? \d\d\d \d\d\d \d\d\d(,)?){3,}") #matches area phone numbers that appear minimum of 3 times and more times in a row...
regex_phone = re.compile(r"((\d\d\d)? \d\d\d \d\d\d \d\d\d(,)?){,5}") #matches area phone numbers that appear minimum of 0 times and maximum of 5 times in a row...
regex_literal = re.compile(r"\*\+\?") #area code can appear one or many times...
# regex_bat = re.compile(r"bat(man|something|money|ton|talion)")
regex_bat = re.compile(r"bat(wo)?man")
regName = re.compile(r"collince") #matches collince
regName = re.compile(r"(ma){3}") #matches ma three times
#above is similar to (r"batman|batwoman), ? indicate that wo can appear one or zero times e.g batwowoman is false

# matchedPhone = regex_phone.findall(large_text)
moName = regName.findall(large_text) #find all thecharacters with name collince
matchedPhone = regex_phone.search(large_text)
matchedLiteral = regex_literal.search(large_text)
matchedBat = regex_bat.search(large_text)

# print("Phone numbers found")
# print(matchedPhone)
# # print("Area code "+str(matchedPhone.group(1)))
# # print(str(matchedPhone.group(2))+" "+str(matchedPhone.group(3)))
# print("\nBats found")
# print(matchedBat.group())

print("\nNames found")
print(moName)
