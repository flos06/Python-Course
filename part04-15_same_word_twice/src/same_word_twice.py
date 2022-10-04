# Write your solution here
num = 0
word = ''
array = []

while True:
    word = input("what word")
    if word in array:
        break
    else:
        array.append(word)
        num += 1

print(f"You typed in {num} different words")
    

