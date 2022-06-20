


def show_hidden_word(secret_word, old_letters_guessed):
    list1=[]
    list1[:0]= secret_word
    number_of_guesses= 4
    while len(old_letters_guessed) < number_of_guesses : 
        x = input("Please guess a letter: ")
        old_letters_guessed.append(x)
        print( old_letters_guessed)
       # i = x
        #for i in str(list1[::1]) : 
         #   if i == str(list1[::1]) : 
          #      y =  list1.replace(str(list1[::1]),"r")
           #     print(y)
            #else:
             #   print("rowmg ansear")
secret_word = "mammals"
old_letters_guessed = []
show_hidden_word(secret_word, old_letters_guessed)
