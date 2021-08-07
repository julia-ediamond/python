import math


class Rectangul:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def calculate_diagonal(self):
        diagonal = math.sqrt((self.height ** 2) + (self.width ** 2))
        return diagonal

    # def is_it_square(self):
    #     if self.width == self.height


my_rectangul = Rectangul(2, 4)
print(my_rectangul.calculate_area())
print(my_rectangul.calculate_perimeter())
print(my_rectangul.calculate_diagonal())
