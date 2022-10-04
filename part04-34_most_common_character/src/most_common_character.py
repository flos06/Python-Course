# Write your solution here
def most_common_character(string):
    mostCommon = ''
    count = 0
    for letter in string:
        if string.count(letter) > count:
            count = string.count(letter)
            mostCommon = letter
    return mostCommon


if __name__ == "__main__":

    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))