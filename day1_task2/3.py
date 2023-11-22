state = 'stop'

states = ['start', 'stop', 'exit']

while True:
    x = input("Enter command (start, stop, exit): ")

    if x == state:
        print(f"Car is already in {x} state")
    
    elif x in states:
        if x == 'exit':
            ans = input("Are you sure you want to exit? (y/n): ")
            if ans.lower() == 'y':
                break
            else:
                continue

        print(f"Car set to {x} state")
        state = x

    else:
        print("Invalid command")    