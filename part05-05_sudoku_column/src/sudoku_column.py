# Write your solution here
def column_correct(sudoku: list, column_no: int):
    newGrid = []

    for row in range(9):

        if sudoku[row][column_no] == 0:
            continue
        elif sudoku[row][column_no] in newGrid:
            return False
        else:
            newGrid.append(sudoku[row][column_no])
    return True

