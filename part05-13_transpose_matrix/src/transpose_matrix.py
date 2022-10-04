# Write your solution here
def transpose(matrix: list):
    newList = []
    for i in range(len(matrix)):
        for item in range(len(matrix[i])):
            newList.append(matrix[item][i])
    
    i = 0

    for row in range(len(matrix)):
        for newItem in range(len(matrix[row])):
            matrix[row][newItem] = newList[i]
            i += 1



# 0,1 must become 1,0 and 0,2 becomes 2,0 - 0,3 becomes 3,0
#1,0 becomes 0,1
# we must loop through column first than append