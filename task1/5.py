def menu():
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exit")

def calculator():
    while True:
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))

        menu()

        x = int(input("enter your choice:"))

        if x == 1:
            print(f"The result is {num1+num2}")
        elif x == 2:
            print(f"The result is {num1-num2}")
        elif x == 3:
            print(f"The result is {num1*num2}")
        elif x==4:
            print(f"The result is {num1/num2}")
        else:
            break

calculator()
