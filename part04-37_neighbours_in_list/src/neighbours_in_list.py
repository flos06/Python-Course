# Write your solution here
def longest_series_of_neighbours(list):
    count = 0
    most = 0
    for num in range(0,len(list) - 1):
        if list[num] == list[num + 1] - 1 or list[num] == list[num + 1] + 1:
            count += 1
            if count > most:
                most = count
        else:
            count = 0
    return most + 1

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))