


def show_hidden_word(secret_word, old_letters_guessed):
    list1=[]
    list1[:0]= secret_word
    u = " ".join(secret_word)
    print (u)
    number_of_guesses= 7

    while len(old_letters_guessed) < number_of_guesses : 
        x = input("Please guess a letter: ")
        old_letters_guessed.append(x)
        y = list1.replace(
        if x == list1 :
            y = list1.replace(
secret_word = "mammals"
old_letters_guessed = []
show_hidden_word(secret_word, old_letters_guessed)
