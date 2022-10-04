# write your solution here



def matrix_sum():
    sum = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            list = line.split(",")

            for num in range(len(list)):
                sum += int(list[num])
    return sum

def matrix_max():
    newlist = []
    maxi = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            list = line.split(",")
            for item in list:
                newlist.append(item)
    maxi = max(newlist)
    return int(maxi)

def row_sums():
    newl = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", '')
            list = line.split(",")
            print(list)
            sum = 0
            for item in list:
                    sum += int(item)

            newl.append(sum)
    
    return(newl)

