is_raining = True
is_cold = True
print(type(is_raining))
print(type(is_cold))
print(is_raining and not is_cold)
print(is_raining)
print(not is_raining)
print(not is_cold)
print(not is_raining and not is_cold)
print(not is_raining and is_cold)


temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print(temperature - wind_chill < 16)

name = "Julia"
print(name == "Julia")
print(name != "Julia")

# if statements

is_raining = False
if is_raining:
    print("Take an umbrella")

if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella.")


if temperature - wind_chill < 16:
    print("Take a jamper")
elif temperature - wind_chill > 30:
    print("It is hot, stay home")
else:
    print("What a lovely day")

# nested if statements
if temperature - wind_chill < 16 and is_raining:
    print("Just stay home")
else:
    if is_raining:
        print("You'll need an umbrella")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today")

# Exercises
# Q1 Kate’scat,Roary,lovescatchingmoths.WriteaprogramthatdetermineswhetherornotitistimeforRoarycatch moths.
moths_in_house = False
moths_in_house = True

if moths_in_house:
    print("Get the moths")
else:
    print("No threats detected")

moths_in_house = False
mitch_is_home = True
if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths")

elif not moths_in_house and not mitch_is_home:
    print("No threats detected")

else:
    if moths_in_house and not mitch_is_home:
        print("Hiis")
    if moths_in_house and mitch_is_home:
        print("Climb on Mitch")
