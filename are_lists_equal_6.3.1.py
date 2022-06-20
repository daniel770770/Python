


def are_lists_equal(list1, list2):
    x = sorted(list1)
    y = sorted(list2)
    if x == y:
        print(True)
    else: 
        print(False)

list1 = [7, 2, 3, 4]
list2 = [2, 3, 4, 1]

are_lists_equal(list1, list2)


