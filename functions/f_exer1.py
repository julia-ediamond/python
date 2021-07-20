# Write a function that takes a temperature in fahrenheitand returns the temperature in celsius.
def temp_in_f_to_c(temp_in_f):

    celsius = (temp_in_f - 32) * 5/9
    return celsius


temp_in_f = 350
celsius = temp_in_f_to_c(temp_in_f)
print(celsius)
