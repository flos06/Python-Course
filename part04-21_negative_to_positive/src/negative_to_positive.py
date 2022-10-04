# Write your solution here
num = int(input('num'))
for i in range(-num, num + 1):
    if i == 0:
        i = 1
    else:
        print(i)