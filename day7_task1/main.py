import book_management as bm
import borrow_return as br
import member_management as mm
import report_generation as rg

def help():
    print("\t1)add book\n\t2) add member\n\t3) view inventory\n\t4) borrow\n\t5) return\n\t6) report\n\t7) update member\
          \n\t8) update book\n\t9) help\n\t10) exit")

bk = bm.Book()
lm = mm.LibraryMember()

while True:
    choice = int(input("Enter your command: "))

    if choice == 1:
        isbn = input("Enter isbn: ")
        title = input("Enter title: ")
        quantity = int(input("Enter quantity: "))
        author = input("Enter author: ")

        bk.add_book(isbn, title, author, quantity)
    
    elif choice==2:
        member_id = input("Enter member id: ")
        name = input("Enter member name")

        lm.add_member(member_id, name)
    
    elif choice==3:
        rg.display_book_inventory(bk)
    
    elif choice==4:
        member_id = input("Enter member id: ")
        isbn = input("Enter isbn: ")
        quantity = int(input("Enter quantity: "))

        br.borrow(bk, lm, member_id, isbn, quantity, "file.json")
    
    elif choice == 5:
        member_id = input("Enter member id: ")
        isbn = input("Enter isbn: ")
        quantity = int(input("Enter quantity: "))

        br.return_bk(bk, lm, member_id, isbn, quantity, "file.json")

    elif choice==6:
        rg.borrowing_reports("file.json") 

    elif choice == 7:
        member_id = input("Enter member id: ")
        name = input("Enter  new name: ")

        lm.update_member(member_id, name)
    
    elif choice==8:
        isbn = input("Enter isbn: ")
        title = input("Enter new title: ")

        bk.update_book(isbn, title)

    else:
        break   