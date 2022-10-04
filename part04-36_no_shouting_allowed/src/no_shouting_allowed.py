# Write your solution here
def no_shouting(list: list):
    newList = []
    for word in list:
        if not word.isupper():
            newList.append(word)
    return newList






if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)