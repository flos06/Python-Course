# Write your solution here
list = []
amount = int(input('amount'))
while amount > 0:
    item1 = int(input('1'))
    list.append(item1)
    amount -= 1
print(list)