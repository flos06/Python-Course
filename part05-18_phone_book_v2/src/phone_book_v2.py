# Write your solution here


def main():
    phoBook = {}
    while True:
        command = int(input("1 search, 2 add, 3 quit"))
        if command == 1:
            search(phoBook)
        if command == 2:
            add(phoBook)
        if command == 3:
            break
    print("quitting...")
    

def add(person):
    name = input("name: ")
    number = input("number: ")
    if name not in person:
        person[name] = []
    person[name].append(number)
    print("ok!")

def search(person):
    name = input("name: ")
    if name not in person:
        print("no number")
    else:
        for number in person[name]:
            print(number)
main()