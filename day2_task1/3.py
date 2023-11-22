book_inventory = []

commands = ["add", "remove", "display", "exit"]

while True:
    x = input("Type one command(add, remove, display, exit)")

    if x not in commands:
        print("Invalid command")
        continue
    
    elif x == "add":
        book = input("Enter a book name: ")

        if book not in book_inventory:
            book_inventory.append(book)
        else:
            print("Book already exists cannot add")
    
    elif x == "remove":
        book = input("Enter a book name: ")

        if book not in book_inventory:
            print("Book doesnot exists")
        else:
            book_inventory.remove(book)
    
    elif x=="display":
        print(f"Current books in the inventory are {book_inventory}")
    
    else:
        x = input("Are you sure you want to exit?(y/n) ")

        if x.lower() == 'y':
            break
