
def fix_age(age):
    if age in [13,14,17,18,19]:
            return 0
    
    return age

def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    
    print(a+b+c)

filter_teens(2,1,15)




#first_number, second_number, third_number = input("Pick 3 numbers: ").split(', ')

#a = int(first_nfilter_teens(14,3,5)umber)
#b = int(second_number)
#c = int(third_number)


#filter_teens(14,3,5)

#def fix_age(age)
#    if age == 13, 14, 17, 18, 19: 
#        print(0)
#    else:
#        print(age)

#print(first_number + second_number + third_number)


#print(first_number + second_number + third_number)

#your_numbers_string = input("Pick 3 numbers: " )
#your_numbers_list = your_numbers_string.split(',') 
#print(your_numbers_list)

#your_fixed_list = map(int, your_numbers_list)
#your_fixed_list = list(your_fixed_list)
#filter_teens(your_fixed_list)
#your_fixed_list_first_number = your_fixed_list[:1]
#your_fixed_list_second_number = your_fixed_list[1:2]
#your_fixed_list_third_number = your_fixed_list[2:]
#x = ((your_fixed_list_first_number) + (your_fixed_list_second_number) + (your_fixed_list_third_number))
#print(x)
#filter_teens(your_fixed_list)
#filter_teens(a, b, c)
