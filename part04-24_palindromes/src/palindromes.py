# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!



def palindromes(str):
    length = len(str)
    newStr = ''

    for char in range(length - 1, -1, -1):
            newStr += str[char]
    if str == newStr:
        print(f"{str} is a palindrome!")
            
        return True
    else:
        print("that wasn't a palindrome")
        return False

while True:
    str = input("input a string")
    if (palindromes(str)):
        break

