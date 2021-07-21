import csv

with open("data1/galaxies.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    slow = [None, float("inf")]
    fast = [None, 0]
    for i, row in enumerate(csv_reader):
        if i != 0:
            if int(row[1]) < slow[1]:
                slow = [row[0], int(row[1])]

            if int(row[1]) > fast[1]:
                fast = [row[0], int(row[1])]
    print(f"Galaxy {slow[0]} has a min velocity of {slow[1]} km/sec")
    print(f"Galaxy {fast[0]} has a max velocity of {fast[1]} km/sec")
