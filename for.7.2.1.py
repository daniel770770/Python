


def is_greater(my_list, n):
    new_list = []
    for x in my_list :
        if x > n:
            new_list.append(x)
            return new_list
#n = 3
#my_list = [ 1, 2, 3, 4, 5]
result = is_greater([1, 2, 3, 4, 5], 4)
print(result)
