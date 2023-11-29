from error_handling import NotExist, NegativeQuantity, TooManyBook
import json
from datetime import date

def check_book_availability(Book, isbn):
    if isbn in Book.book_inventory:
        return True
    return False
    
def update_book_quantity(Book, isbn, quantity, increase=None, decrease=None):

    if not check_book_availability(Book, isbn):
        raise NotExist

    if quantity < 1:
        raise NegativeQuantity

    if not isbn in Book.book_inventory:
        raise NotExist
    
    x = Book.book_inventory[isbn]

    if increase:
        x['quantity'] += quantity
        print("Quantity increased")
    
    else:
        if quantity > x['quantity']:
            raise TooManyBook

        x['quantity'] -= quantity

def write_file(file, isbn, member_id, quantity, borrow=False):
    with open(file, 'r') as f:
        jsn = json.load(f)
    
    if member_id in jsn:
        flag = False
        for x in jsn[member_id]:
            if isbn in x:

                flag = True

                idx = jsn[member_id].index(x)

                if borrow:
                    print("Return your books to get take the similar ones")
                    return
                
                val = x[isbn]

                if quantity > val['quantity']:
                    print("You cannot return more books than you have borrowed")
                    return
                
                elif quantity == val['quantity']:
                    del jsn[member_id][idx][isbn]
                
                else:
                    jsn[member_id][idx][isbn]['quantity'] -= quantity

        if borrow and not flag:
            jsn[member_id].append({isbn: {'quantity': quantity, 'date': date.today()}})
        else:
            raise NotExist
    
    else:
        if borrow:
            jsn[member_id] = {isbn: {'quantity': quantity, 'date': date.today()}}
        else:
            raise NotExist
    
    ans = json.dumps(jsn)

    with open(file, 'w') as f:
        f.write(ans)
        
def borrow(Book, library, member_id, isbn, quantity, file):
    if member_id not in library.members_list:
        raise NotExist

    update_book_quantity(Book, isbn, quantity, None, True)

    write_file(file, isbn, member_id, quantity, borrow=True)


def return_bk(Book, library, member_id, isbn, quantity, file):
    if not member_id in library.member_list:
        raise NotExist
    
    update_book_quantity(Book, isbn, True, None)
    write_file(file, isbn, member_id, quantity, borrow=False)