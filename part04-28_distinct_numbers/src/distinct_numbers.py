# Write your solution here
def distinct_numbers(list):
    arr = []
    for num in range(len(list)):
        if list[num] not in arr:
            arr.append(list[num])
    arr.sort()

    return arr

