""" program checks if a given string is a phone number
the phone number is checked if it follows the standard format
"""

#function checks if a string is a phone number
#returns true or false depending on the attributes
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
         if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
         if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


textString= input('Enter a string: ')
print(textString)

x=isPhoneNumber(textString)
print(x)
    


