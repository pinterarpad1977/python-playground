'''
Create two classes:
1. Author
Attributes:
• name
• nationality
Method:
• describe() → returns a string

2. Book
Attributes:
• title
• year
• author (this should be an Author object)
Method:
• details() → returns a string including the author’s description
'''


class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def describe(self):
        return f"{self.name} from {self.nationality}"
    
class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def details(self):
        return (
            f"{self.title} written by " 
            f"{self.author.nationality} " 
            f"author {self.author.name} " 
            f"in {self.year}.")
    
a = Author("George Orwell", "British")
b = Book("1984", 1949, a)

print(b.details())