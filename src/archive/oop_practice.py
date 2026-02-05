'''
Create a class called Book with:
• title
• author
• year
• a method age() that returns how old the book is
• a method describe() that prints a nice summary
'''
from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year
    
    def describe(self):
        return (
            f"'{self.title}' by {self.author}, "
            f"published in {self.year} "
            f"({self.age()} years old)."
        )
    
"""     
now1 = datetime.now()
print(type(now1.year))
 """

b1 = Book("Socks", "Arpad", 2022)
print(b1.age())
print(b1.describe())