# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_book=0    #class variable

    def __init__(self,name):   
        self.name=name
        Book.increment_book_count()

    @classmethod                #class method or function its use in class not instance or object
    def increment_book_count(cls):
        cls.total_book+=1

    @classmethod
    def get_total_books(cls):
           return cls.total_book


book1=Book("english")
book2=Book("math")
book3=Book("physic")
print(f"Total Book is : {Book.get_total_books()}")