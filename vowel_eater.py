#

# Prompt the user to enter a word
# and assign it to the user_wYour task here is very special:
#you must design a vowel eater! Write a program that uses:

#a for loop;the concept of conditional execution (if-elif-else)
#the continue statement.Your program must:ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate line.ord variable.

user_word=input("Enter a word:")
user_word=user_word.upper()
#letter=(a,e,i,o,u)

for letter in user_word:
    #if letter != ['A','e','i','o','u']:
        #continue
        if letter == 'A':
            continue
        elif letter=='E':
            continue
        elif letter=='I':
            continue
        elif letter=='O':
            continue
        elif letter=='U':
            continue

        print(letter)
    #else:
        
        
    
