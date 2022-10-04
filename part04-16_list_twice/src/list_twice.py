# Write your solution here
array = []
while True:
    item = int(input("item"))
    if item == 0:
        break
    array.append(item)
    print(f"The list now: {array}")
    print(f"The list in order: {sorted(array)}")
print("Bye!")