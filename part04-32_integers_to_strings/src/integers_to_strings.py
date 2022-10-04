# Write your solution here
def formatted(list):
    arr = []
    for num in range(len(list)):
        arr.append(f"{list[num]:.2f}")
    print(arr)
    return arr

