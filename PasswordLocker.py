#! python3
# pw.py - An insecure password locker program.
"""
password locker manages the passwords for different site, user can copy the password
for the site to the clipboard no need to  memorize it
"""
#store the passwords in dictionaries
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
#sys.argv has two arguments:
#1. the  progam filename
#2. the first command line argument

#pyperclip modules ensures that u copy the key’s value to the clipboard using pyperclip.copy()
import sys, pyperclip
if len(sys.argv) < 2: #parse 2 arguments, the message will display if user forget

    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
#argument parsing
account = sys.argv[1]    # first command line arg is the account name

#account should be the key for the dictionaries
if account in PASSWORDS: #dictionary defined above
    pyperclip.copy(PASSWORDS[account]) #copying password for the account to clipboard
    print('Password for ' + account + ' copied to clipboard.')
else:
    #if the account isnt available
    print('There is no account named ' + account)
"""
create a program that takes in the account and password as input and store
in a file, then retrieve later on.
user to input the account required and the password in copied to the clipboard
"""
