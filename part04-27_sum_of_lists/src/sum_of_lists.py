# Write your solution here

def list_sum(list1, list2):
    arr = []
    for num in range(len(list1)):
        arr.append(list1[num] + list2[num])
    return arr
