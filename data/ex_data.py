import csv

with open('data1/colours_20.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    next(csv_reader)
    for colour in csv_reader:
        #full_name = colour[-2:]
        full_name = colour[2:]
        full_name = " ".join(full_name)
        print(
            f"RGB: {colour[0]}, HEX: {colour[1]}, English: {full_name}")


# with open("data1/colours_20.csv") as csv_file:
#   csv_reader = csv.reader(csv_file, delimiter=",")
#   for i, row in enumerate(csv_reader):
#        if i != 0:
#           print(f"{row[2]}, HEX: {row[1]}, RGB: {row[0]}")
