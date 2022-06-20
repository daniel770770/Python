


def sequence_del(my_str):
    current_letter = []
    new_str = []
    for letter in my_str:
        if letter != current_letter :
            new_str += letter
            current_letter = letter 
    return new_str

print(sequence_del('aaabbbccc'))

