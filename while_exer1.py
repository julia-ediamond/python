#user_input = 0
#desired_input = ""
#numbers = []
#user_input = input("Enter a number: ")
# while user_input != desired_input:

#    if user_input != "":
#        user_input = input("Enter a number: ")
#        user_input = int(user_input)
# numbers.append(user_input)

# numbers.pop(-1)
#total = sum(numbers)
# print(total)

number = input("Enter a number: ")
total = 0

while number != "":
    total = total + int(number)
    number = input("Enter a number: ")
print(total)
