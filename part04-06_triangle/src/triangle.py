# Copy here code of line function from previous exercise

def triangle(size):
    # You should call function line here with proper parameters
    x = 0
    while x <= size:

        line(x, "#")
        x += 1



def line(num, str):
    if len(str) != 0:
        print(num * str[0])
    else:
        print('*' * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
