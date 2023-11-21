sentence = str(input("Enter a sentence: "))

count = 0

for s in sentence:
    if s in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Total vowel is {count}")