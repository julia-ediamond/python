import csv

with open('data\data1\employee_birthday.csv', mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')

        print(
            f'\t{row["name"]} works in the {row[" department"]} department, and was born in {row[" birthday month"]}.')
        line_count += 1
    print(f"Processed {line_count} lines.")
