import csv

asli_said = []

with open("dogs.txt", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)  # creates reader object
    for line in csv_reader:
        # print(line)
        asli_said.append(line)
print(asli_said)

# creates a new file, if file exists, it will be overwritten
with open("asli_says.txt", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)  # creates writer object
    for item in asli_said:
        csv_writer.writerow(item)
# newline will put everything on new lines
