# Write your solution here

def remove_smallest(numbers: list):
    newL = []
    small = numbers[0]
    for num in range(len(numbers)):
        if numbers[num] < small:
            small = numbers[num]
    for num in range(len(numbers)):
        if numbers[num] == small:
            continue
        else:
            newL.append(numbers[num])
    numbers[:] = newL




if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)