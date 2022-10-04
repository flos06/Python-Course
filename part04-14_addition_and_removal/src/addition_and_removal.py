# Write your solution here
list = []
item = ''
num = 1
print(f"The list is now {list}")
while item != 'x':
    
    item = input("add remove or exit")
    if item == 'd':
        list.append(num)
        num += 1
        print(f"The list is now {list}")
    if item == 'r':
        list.pop()
        num -= 1
        print(f"The list is now {list}")
print("Bye!")