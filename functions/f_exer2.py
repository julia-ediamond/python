# Writeafunctionthatacceptsoneparameter(aninteger)andreturnsTruewhenthatparameterisoddandFalse when that parameter is even.
def odd(number):
    return number % 2 != 0


odd_number = odd(62)
odd_number = odd(63)
print(odd_number)
