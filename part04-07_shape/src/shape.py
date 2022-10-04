# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def shape(width, char, height, filler):
    x = 0
    i = 0
    while x <= width:

        line(x, char)
        x += 1
    while i < height:
        line(width, filler)
        i += 1



def line(num, str):
    if len(str) != 0:
        print(num * str[0])
    else:
        print('*' * num)
if __name__ == "__main__":
    shape(5, "x", 2, "o")

