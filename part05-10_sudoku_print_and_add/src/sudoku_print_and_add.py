# Write your solution here

def print_sudoku(sudoku: list):
    for row in range(9):
        print()
        colEnd = 0
        if row == 3 or row == 6:
            print('')
        for item in range(9):
            if colEnd == 3 or colEnd == 6:
                print(' ', end='')
            if sudoku[row][item] == 0:
                print("_ ", end='')
                colEnd += 1
            else:
                print(sudoku[row][item], '', end='')
                colEnd += 1



def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    print(sudoku)


