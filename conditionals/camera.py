# Write a program that implements the algorithmfor Red Light Cameras.
light_colour = "Green"
car_detected = False

if light_colour == "Red" and car_detected:
    print("Do nothing")
elif light_colour and not car_detected:
    print("Flash")
elif light_colour == "Green" and not car_detected:
    print("Do nothing")
elif light_colour == "Amber" and car_detected:
    print("Do nothing")
elif light_colour == "Amber" and not car_detected:
    print("Do nothing")
