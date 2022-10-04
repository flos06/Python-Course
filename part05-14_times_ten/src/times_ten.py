# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict = {}
    for key in range(start_index, end_index + 1):
        dict[key] = key * 10
    return dict