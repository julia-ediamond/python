# Ask the user to enter a string. Output the stringone character at a time, as well as it’s positionin the string
user_input = input("Enter a word or a phrase: ")
for i, letter in enumerate(user_input, start=0):
    print(i, letter)
