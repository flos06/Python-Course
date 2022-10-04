# Write your solution here

def even_numbers(list):
    arr = []
    for num in range(len(list)):
        if list[num] % 2 == 0:
            arr.append(list[num])
    return arr