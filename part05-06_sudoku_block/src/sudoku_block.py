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


