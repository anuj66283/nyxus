import re


class Accounts:
    
    accs = {}

    def validate(password):
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
        return bool(re.match(pattern, password))

    @classmethod
    def add_user(cls, user_id, password):
        if user_id in cls.accs:
            print("User alrady exists")
            return False
        
        if cls.validate(password):
            cls.accs[user_id] = password
            print("Added successfully")
            return True

        print("Cannot validate password")
        return False

acc = Accounts()

while True:
    user_id = input("Enter user_id: ")
    password = input("Enter password: ")

    if acc.add_user(user_id, password):
        x = input("Do you want to add another user?(y/n): ")
        if x.lower() == 'y':
            continue
        break