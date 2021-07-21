import csv

#found_colors = []


def find_colour(english_colour):
    colour_count = 0
    with open('data1/colours_20.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        next(csv_reader)
        for (index, colour) in enumerate(csv_reader):
            english_colour_match = english_colour == colour[2]
            if english_colour_match:
                for english_colour in colour[2]:
                    colour_count += 1
                #counts = {}
                # for english_colour in csv_reader:
                # c = Counter(english_colour
                #            for colour[2] in csv.reader(csv_file))
                # found_colors.append(english_colour)
                #counts[english_colour] = counts.get(english_colour, 0) + 1
                # for c in csv_reader:           # update counts from an iterable
                #    c = Counter(int([english_colour]))
                return (f"{english_colour} found {colour_count} times.")
        return (f"{english_colour} not found")


response = find_colour("Brown")
print(response)
