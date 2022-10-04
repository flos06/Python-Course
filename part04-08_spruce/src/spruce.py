# Write your solution here
def spruce(height):
    ast = 1
    print('a spruce!')
    while height > 0:
        
        print((height - 1) * ' ', end = '')
        print(ast * '*')
        ast += 2
        height -= 1

    print((ast // 2  - 1 )* ' ' + '*')
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)