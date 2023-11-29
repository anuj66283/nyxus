from error_handling import NegativeQuantity, AlreadyExists, NotExist, TooManyBook

class Book:
    book_inventory = {}

    @classmethod
    def add_book(cls, isbn, title, author, quantity):
        rslt = {
            'title': title,
            'author': author,
            'quantity': quantity
        }

        if isbn in cls.book_inventory:
            raise AlreadyExists

        cls.book_inventory[isbn] = rslt

        print("Added successfully")


    @classmethod
    def update_book(cls, isbn, name):
        
        if isbn not in cls.book_inventory:
            raise NotExist
        
        cls.book_inventory[isbn]['name'] = name


    @classmethod
    def remove_book(cls, isbn):
        if isbn not in cls.book_inventory:
            raise NotExist
        
        del cls.book_inventory[isbn]