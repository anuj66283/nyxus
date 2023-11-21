import random

x = random.randint(1, 100)

for _ in range(3):
    guess = int(input("Enter a number: "))
    if x == guess:
        print("You're correct")
        break

    elif x>guess:
        print('higher')
    
    else:
        print("lower")
