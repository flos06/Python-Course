# Write your solution here
def mean(list):
    length = len(list)
    x = 0
    sum = 0
    while x < length:
        sum += list[x]
        x += 1
    return sum / length

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 1, 3, 4, 4, 5, 7, 7, 23, 67]
    result = mean(my_list)
    print(result)