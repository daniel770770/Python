#The hangman game 

#bag check

def is_valid_input(letter_guessed):
    """
    This function make a bag check 
    :is_valid_input: The number that the player pick.
    :type is_valid_input: int
    :return: 
    If there is more than one number= "E1"
    If there is a letter that is a character= "E2"
    If there is both= "E3"
    """
    guess_len = len(letter_guessed)
    one_letter = (letter_guessed[0:1])
    lower_letter = one_letter.lower()
    x = letter_guessed.isalpha()
    if guess_len > 1 and x == 0:
        print("E3")
    elif guess_len > 1:
        print("E1")
    elif x == 0:
        print("E2")
    else:
        print(lower_letter)


def main():
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


#The system will pick a random number and print it

    import random
    n = random.randint(4,10)
    print(n)


#The player will ask to guess a letter.

    letter_guessed = input("Guess a letter: ")

#The letter now will be go through the "is_valid_input" for bag check.

    is_valid_input(letter_guessed)

#The player will ask to guess a word
   word = input("Please enter a word: ")

#prints the lower lines 

    lower= "_ " * len(word)
    print (lower)

if __name__ == "__main__":
    main()
#The end

