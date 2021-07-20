#moths_in_house = True
#mitch_is_home = True
moths_in_house = False
mitch_is_home = True
if moths_in_house and mitch_is_home:
    #   print("Get the moths!")
    print("Hoooman! Help me get the moths!")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch")
else:
    print("No threats detected")
