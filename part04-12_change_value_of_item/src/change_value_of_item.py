# Write your solution here
list = [1, 2, 3, 4, 5]
index = 0
while True:
    index = int(input('index'))
    if index == -1:
        break
    value = int(input('value'))
    list[index] = value

    print(list)