# write your solution here
def read_fruits():
    dict = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            list = line.split(";")
            dict[list[0]] = float(list[1])
    return dict

