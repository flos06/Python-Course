# Write your solution here
def no_vowels(string):
    vowels = 'aoeiu'
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, '')

    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))