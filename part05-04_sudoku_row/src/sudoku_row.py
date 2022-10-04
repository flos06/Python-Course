# Write your solution here

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
                




