


def format_list(my_list):
    y = my_list[0:-1:2]
    x = my_list[-1]
    y = ", ".join(y)
    print(y+", and " +x)


my_list = ["I", "am", "a", "Devops"]
format_list(my_list)
