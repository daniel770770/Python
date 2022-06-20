#This app take a list and move the objects one place to the left


def shift_left(my_list):
    a, b, c = my_list
    left_list= b, c, a
    return left_list

my_list =[1, 2, 3]
print(shift_left(my_list))
