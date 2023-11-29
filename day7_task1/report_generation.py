import json

def display_book_inventory(book):
    for x in book.book_inventory:
        print(f'isbn: {x} name: {book.book_inventory[x]["title"]} quantity: {book.book_inventory[x]["quantity"]}')
    
def borrowing_reports(file):
    with open(file, 'r') as f:
        jsn = json.load(f)

    for x in jsn:
        for y in x:
            for z in y:
                print(f'member_id: {x} isbn: {z} quantity: {y["quantity"]} date: {y["date"]}')