def arrow(my_char, max_length):
    for i in range(1, max_length * 2):
        if i <= max_length:
            print('*' * i )
        else:
            print('*' * (max_length  * 2 -i))

arrow('*', 50)
