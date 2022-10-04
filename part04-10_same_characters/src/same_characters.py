# Write your solution here
def same_chars(str, num1, num2):
    if num1 > len(str) - 1 or num2 > len(str) - 1:
        return False
    elif str[num1] == str[num2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))