# This is a code for check waht day it is for a specific date

import calendar

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

input_date = input("What is the date that you whant to check? (in DD/MM/YYYY)")

day = input_date[:2]
months = input_date[3:5]
years = input_date[6:]

day_int = int(day)
months_int = int(months)
years_int = int(years)

final_answer = (calendar.weekday(years_int, months_int, day_int))
final_answer_string = weekdays[final_answer]
print(final_answer_string)




#print("in that date the day was {}".format(final_answer_string))
