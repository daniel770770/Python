



def numbers_letters_count(my_str):
    results_list = [0, 0]
    for i in my_str:
        if i >= '0' and i <= '9':
            results_list[0] += 1
        else:
            results_liist[1] += 1
    return results_list
      

my_str = str("1fgre43")
x = numbers_letters_count(my_str)
print(x)
