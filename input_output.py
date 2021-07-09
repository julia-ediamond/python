# Q1
num1 = 3
num2 = 9
calc1 = num1 + num2
print(f"Enter a number {num1}")
print(f"Enter a number {num2}")
print(float(calc1))

num3 = -3
print(f"Enter a number {num3}")
print(f"Enter another number {num2}")
calc2 = num2 + num3
print(float(calc2))

num4 = 3.0
num5 = -9
print(f"Enter a number: {num4}")
print(f"Enter another number: {num5}")
calc3 = num5 - num3
print(float(calc3))

# Q2
print(f"Enter a number: {num1}")
print(f"Enter another number: {num2}")
calc4 = float(num1) * float(num2)
print(f"{float(num1)} * {float(num2)} = {float(calc4)}")

print(f"Enter a number: {num3}")
print(f"Enter another number: {num2}")
calc4 = float(num3) * float(num2)
print(f"{float(num3)} * {float(num2)} = {calc4}")

print(num4)
print(num5)
print(f"Enter a number: {num4}")
print(f"Enter another number: {num5}")
calc5 = num4 * num5
print(f"{num4} * {num5} = {calc5}")


# Q3
number_kilometers = 10
distance = "km"
distance_m = "m"
distance_cm = "cm"
question = "How many kilometres?"
print(question + str(number_kilometers))

km_to_m = number_kilometers * 1000
print(f"{number_kilometers} {distance} = {km_to_m} {distance_m}")

km_to_cm = number_kilometers * 100000
print(f"{number_kilometers} {distance} = {km_to_cm} {distance_cm}")

number_kilometers = 5.4
km_to_m = number_kilometers * 1000
km_to_cm = number_kilometers * 100000
print(question + str(number_kilometers))
print(f"{number_kilometers} {distance} = {int(km_to_m)} {distance_m}")
print(f"{number_kilometers} {distance} = {int(km_to_cm)} {distance_cm}")

# Q4
name = "William"
height = 192
height_question = "How tall are you (cms)?"
name_question = "What is your name?"
print(f"{name_question} {name}")
print(f"{height_question} {height}")
print(f"{name} is {height} cms tall.")

name = "Chilli"
height = 27
print(f"{name_question} {name}")
print(f"{height_question} {height}")
print(f"{name} is {height} cms tall.")
