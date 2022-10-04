# Write your solution here# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    num = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                num += 1
    return num