# Write your solution here





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

def row_correct(sudoku: list, row_no: int):
    rowItem = []

    for item in sudoku[row_no]:
        if item == 0:
            continue
        elif item in rowItem:
            return False
        else:
            rowItem.append(item)
    return True
                


def block_correct(sudoku: list, row_no: int, column_no: int):
    newGrid = []
    for row in range(row_no, row_no + 3):
        for item in range(column_no, column_no + 3):
            if sudoku[row][item] == 0:
                continue
            if sudoku[row][item] in newGrid:
                print(sudoku[row][item])
                print(newGrid)
                return False
            else:
                newGrid.append(sudoku[row][item])
    
    return True

#start at 0, 0
# + 3, + 3

def sudoku_grid_correct(sudoku: list):
    j = 0
    array = [0,0,0,3,0,6,3,0,3,3,3,6,6,0,6,3,6,6]
    for i in range(9):
        if row_correct(sudoku, i) and column_correct(sudoku, i) and block_correct(sudoku, array[j], array[j+1]):
            
            j += 2
                
            continue
        else:
            return False
    return True

