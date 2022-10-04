# Write your solution here

def length_of_longest(list):
    longest = 0
    for string in range(len(list)):
        if len(list[string]) > longest:
            longest = len(list[string])
    return longest


