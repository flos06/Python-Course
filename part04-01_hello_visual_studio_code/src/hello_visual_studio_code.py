# Write your solution here
edit = ''

while edit != 'visual studio code':
    edit = input("editor?")
    edit = edit.lower()

    if edit == 'word':
        print("awful")
    elif edit == 'notepad':
        print("awful")
    elif edit == 'visual studio code':
        break
    else:
        print("not good")

print("an excellent choice!")