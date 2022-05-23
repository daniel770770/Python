my_str = input("Pick a word: ")

def last_early(my_str):
    my_str.lower()
    if my_str.count(my_str[-1]) > 1:
        print("True")
    else:
        print("False")

last_early(my_str)


#my_str = input("Pick a word: ")


