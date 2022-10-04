# Copy here code of line function from previous exercise

def square(size, character):
    # You should call function line here with proper parameters
    x = size
    while x > 0:

        line(size, character)
        x -= 1



def line(num, str):
    if len(str) != 0:
        print(num * str[0])
    else:
        print('*' * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")