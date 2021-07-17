def convert_cm_to_in(length_cm):

    length_in_inch = length_cm / 2.54
    return length_in_inch


print(convert_cm_to_in(20))

# print(length_in_inch)  # is not defined
# inches to cm


def convert_in_to_cm(length_in):
    length_in_cm = length_in * 2.54
    return length_in_cm


print(convert_in_to_cm(10))


def add(a, b):
    #result = a + b
    # return result
    return a+b


print(add(2, 3))


def calc_mean(a, b):
    total = a + b
    mean = total / 2
    return mean


print(calc_mean(3, 4))
