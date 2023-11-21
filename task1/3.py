def get_list(n):
    lst = []

    for _ in range(len(n)):
        x = int(input("Enter a number: "))
        lst.append(x)

    return lst

def find_sum():
    n = int(input("How many number do you want to add? "))
    
    lst = get_list(n)

    odd_sum = 0
    even_sum = 0

    for x in lst:
        if x%2==0:
            even_sum += x
        else:
            odd_sum += x
    
    print(f'Even sum is {even_sum} and odd sum is {odd_sum}')

find_sum()