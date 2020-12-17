"""
1. Paste text from the clipboard -pyperclip.paste()
2. Do something to it- add bullets *
3. Copy the new text to the clipboard -pyperclip.copy()
"""
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste() #copy text to the clipboard
# Separate lines and add stars.
lines = text.split('\n') #after every new line add * before the follwoing line

for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
    """
To make this single string value, pass lines into the join() method to get a
single string joined from the list’s strings
"""
text = '\n'.join(lines)
pyperclip.copy(text)
