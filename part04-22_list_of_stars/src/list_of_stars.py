# Write your solution here
def list_of_stars(list):
    for i in range(len(list)):
        print(list[i] * '*')


if __name__ == "__main__":
    list = [3, 2, 1, 6, 7]
    print(list_of_stars(list))