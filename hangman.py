#The hangman game 

#intro screen

ANGMAN_ASCII_ART = (
 """Welcome to the game Hangman \n
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \.
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/""")

print(ANGMAN_ASCII_ART)


#The system will pick a random number

import random
n = random.randint(4,10)
print(n)

 
#The player will ask to guess a letter.

Guess = input ("Guess a letter: ")
guess_len = len(Guess)
one_letter = (Guess[0:1])
lower_letter = one_letter.lower()


#bag_check = word

x = Guess.isalpha()

if guess_len > 1 and x == 0:
    print("E3")
elif guess_len > 1:
    print("E1")
elif x == 0:
 print("E2")
else:
    print(lower_letter)


#The player will ask to guess a word

word = input ("Please enter a word: ") 



#print the lower lines 

lower= "_ " * len(word)
print (lower)



