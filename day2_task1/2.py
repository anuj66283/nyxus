set1 = set()
set2 = set()

print("Pass a string to end loop")

while True:
    x = input("Enter a number")
    try:
        x = int(x)
        set1.add(x)
    except:
        print("Integer not found ending the loop")
        break

while True:
    x = input("Enter a number")
    try:
        x = int(x)
        set2.add(x)
    except:
        print("Integer not found ending the loop")
        break


print(f"Intersection is {set1.intersection(set2)}")
print(f"Union is {set1.union(set2)}")
