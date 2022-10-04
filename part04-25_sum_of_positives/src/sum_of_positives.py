# Write your solution here
def sum_of_positives(list):
    sum = 0
    for num in range(len(list)):
        if list[num] > 0:

            sum += list[num]
    return sum

if __name__ == "__main__":
    list = [1, -1, 2, -2, 3, -3]
    sum_of_positives(list)