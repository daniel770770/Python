

input_number_1 = input("Pick the first number: ")
input_number_2 = input("Pick the second number: ")
input_number_3 = input("Pick the third number: ")


def distance(num1, num2, num3):
    number = (num2 - num1)
    number_a = (num3 - num1)
    number_b = (num3 - num2)
    absolute_number = abs(number)
    absolute_number_a = abs(number_a)
    absolute_number_b = abs(number_b)
    if absolute_number == 1 or absolute_number_a == 1 and absolute_number_a > 2 or absolute_number_b > 2 :
        print("True")
    else: 
        print("False")



distance(int(input_number_1), int(input_number_2), int(input_number_3))
# or number_b > 1 :

