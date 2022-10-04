# # Write your solution here


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
    person[name] = number
    print("ok!")

def search(person):
    name = input("name: ")
    if name in person:
        print(f"{person[name]}")
    else:
        print("no number")
main()