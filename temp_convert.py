#Convert temperature from c/C to f/F and from f/F to c/C


degrees = input("what is the temperature you would like to convert: ")

fahrenheit_or_celsius = degrees[-1::1]
temperature = degrees[:-1]
temperature_number = int(temperature)

if 'f' in fahrenheit_or_celsius or 'F' in fahrenheit_or_celsius:
    print((temperature_number * 5 - 160) // 9, "c")
elif 'c' in fahrenheit_or_celsius or 'C' in fahrenheit_or_celsius:
    print((temperature_number * 9 + 160) // 5, "f")

