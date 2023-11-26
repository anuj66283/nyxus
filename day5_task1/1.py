students = []

roll = 0


class student:
    def __init__(self, name, marks):
        global roll
        self.name = name
        self.roll_no = roll
        self.marks = marks
        roll += 1
    
    def __str__(self):
        return f'Name: {self.name} Roll_no: {self.roll_no} Marks: {self.marks}'

def check_integer(string):
    x = input(f"Enter {string}: ")
    try:
        x = int(x)
        return x, 1
    except:
        print("Please use integer to integer")
        return x, 0
    
def add_student():
    nam = input("Enter the student name: ")    
    
    marks, flag = check_integer('marks')

    if not flag:
        return
    
    stu = student(nam, marks)
    students.append(stu)

def view_all():
    if not students:
        print("List is empty")
        return

    print("Here is the info about all students")

    for x in students:
        print(x)

def find_student(x):
    if not students:
        print("List is empty")
        return 0, 0

    for stu in students:
        if stu.roll_no == x:
            print("Student found")
            print(stu)
            return students.index(stu), 1
        
    print("Student not found")
    return 0, 0

def update_student(x):
    val = input("What do you want to update?(name, marks)")

    if val == "name":
        val = input("Enter a name")
        students[x].name = val
        print("Successfully added")
        return
    
    elif val == 'marks':
        #val = input("Enter marks")

        val, flag = check_integer('marks')

        if not flag:
            return
        
        students[x].marks = val
        print("Successfully added")

    else:
        print("Invalid input")
        return

def delete_student(x):    
    del students[x]
    print("Successfully deleted")

def sort_marks():
    if not students:
        print("Empty list")
        return

    students.sort(key=lambda x: x.marks)
    print("Sorted students")

def help():
    print("Here are list of commands:\n\t1) add\n\t2) view_all\n\t3) find\n\t4) update\n\t5) delete\n\t6) sort\n\t7) help\n\t8) exit")

help()

while True:

    choice = int(input("Enter your choice number: "))

    if choice == 1:
        add_student()
        continue
    
    elif choice == 2:
        view_all()
        continue

    elif choice == 3:
        x, flag = check_integer('roll_no')

        if not flag:
            break

        find_student(x)
        continue

    elif choice == 4:
        x, flag = check_integer('roll_no')

        if not flag:
            break
        
        x, flag = find_student(x)

        if not flag:
            break

        update_student(x)

        continue
    
    elif choice == 5:
        x, flag = check_integer('roll_no')

        if not flag:
            break
        
        x, flag = find_student(x)

        if not flag:
            break

        delete_student(x)
        continue

    elif choice == 6:
        sort_marks()
        continue

    elif choice == 7:
        help()
        continue
    
    elif choice == 8:
        break

    else:
        print("Invalid command")
        help()
        continue



    

