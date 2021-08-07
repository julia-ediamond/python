class Book:
    #attributes - size, pages, colour
    # methods = turning a page, opening, closing
    def __init__(self, title, author, pages, current_page):
        # assignment to object attributes
        self. title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1  # assigned to 1 by default

    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self):
        #self.current_page += 1
        if self.current_page == self.pages - 1:
            self.current_page == 1
        else:
            self.current_page += 1

    # str representation

    def __str__(self):
        return f"Title:{self.title}, Author: {self.author}, Page: {self.pages}"

    def __len__(self):
        return self.pages
    # create a method turn the page back

    def turn_back(self):
        self.current_page -= 5

    def specific_page(self):
        self.bookmark = 100
        return self.bookmark

    def back_to_start(self):
        if self.current_page >= self.pages:
            self.current_page == 1


my_book = Book("A great book", "me", 362, 14)
print(my_book)
print(my_book.__str__())  # this is what is happening behind the scenes
print(my_book)
print(my_book.bookmark)  # attr
# my_book.turn_page()  # method
print(my_book.bookmark)
my_book.turn_back()
print(my_book.bookmark)
print(my_book.specific_page())


class Employee:
    # attr (self, name, role, )
    # method work , get_name, get_role
    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return(self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone_number)


employee_1 = Employee("Fran", 78000, "212121212", "1 June 2020")
employee_1.get_employment_details()
print(employee_1.get_contact_details())
