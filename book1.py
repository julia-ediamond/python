import sqlite3
connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
DROP TABLE IF EXISTS books
""")

cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY, 
    title TEXT, 
    pages INTEGER, 
    current_page INTEGER
)
""")


cursor.execute("""
INSERT INTO books VALUES (
    0, "A great book", 213, 27

)

""")
cursor.execute("""
INSERT INTO books VALUES (
    1, "Another great book", 395, 387

)

""")

rows = cursor.execute("""
SELECT * FROM books 

""")

rows = cursor.execute("""
SELECT title FROM books where id=1

""")
rows = cursor.execute("""
SELECT id FROM books where title="A great book"

""")

rows = cursor.execute("""
DELETE FROM books where id=0

""")

rows = cursor.execute("""
UPDATE books SET current_page = 26 WHERE id=1

""")


def calculate_read_time():
    read_speed = input("How many pages do you read per minute?")
    for row in rows:
        read_time = row[1] / float(read_speed) / 60
    print("Book:", row)
    print("%.2f" % read_time, "hours to read", row[0])


calculate_read_time()
for row in rows:
    print(row)

connection.commit()
connection.close()
