import csv

colour_dict = {}
with open('data/data1/colours_20.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    next(csv_reader)
    for line in csv_reader:
        # the value in the secon item, the value is going to be 2
        #colour_dict[line[1]] = line[2]
        # create empty list and inject them inside
        colour_dict[line[1]] = [line[0], line[2]]
        #print(f"{line[1]} {line[2]} ")
print(colour_dict)
