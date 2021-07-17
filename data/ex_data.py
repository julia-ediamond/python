import csv


with open("data1/colors.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')  # creates reader
    for row in csv_reader:
        print(row)
        # for i in enumerate(csv_reader):
        #    if i != 0:
        #        print(f"{row[2]}, HEX: {row[1]}, RGB: {row[0]}")
