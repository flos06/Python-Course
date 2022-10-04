# Write your solution here
def first_word(str):
    index = str.find(' ')
    return str[0:index]
def second_word(str):
    index = str.find(' ')
    str = str[index + 1:] 
    index2 = str.find(' ')
    if index2 == -1:
        return str[0:]
    else:
        return str[0:index2]
def last_word(str):
    x = 0
    while x < len(str):
        if str[x] == ' ':
            index = x + 1
        x += 1
    return str[index:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))