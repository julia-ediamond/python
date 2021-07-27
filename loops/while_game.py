# Q3 Selectanumber.Asktheusertoenteranumber,outputwhethertheirnumberislessthanorgreaterthanthe selected number. Repeat this process until theuser guesses the correct number.

goal_number = 5
user_guess = 0  # give guess a starting value
while user_guess != goal_number:
    user_guess = int(input("Guess a number: "))
    if user_guess < goal_number:
        print("Too low")
    if user_guess > goal_number:
        print("Too high")
print("This is the right guess!")
