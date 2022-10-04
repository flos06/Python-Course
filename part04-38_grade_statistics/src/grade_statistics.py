# Write your solution here

def input_user():
    count = 0
    examAndExcer = 0
    fail = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    while True:
        resp = input("Points and exercizes completed")
        if resp == '':
            break
        
        
        points, exerc = resp.split(' ')
        points, exerc = int(points), int(exerc)
        count += 1
        exPoints = exerPoints(exerc)
        grade, totPoints = grades(points, exPoints)
        examAndExcer += totPoints
        if grade == 0:
            fail += 1
        elif grade == 1:
            grade1 += 1
        elif grade == 2:
            grade2 += 1
        elif grade == 3:
            grade3 += 1
        elif grade == 4:
            grade4 += 1
        else:
            grade5 += 1
    average = round(examAndExcer / count, 1)
    passP = round((grade1 + grade2 + grade3 + grade4 + grade5) / count * 100, 1)
    printStats(average, passP, fail, grade1, grade2, grade3, grade4, grade5)

def printStats(average, passP,fail, grade1, grade2, grade3, grade4, grade5):
    gr0 = fail * "*"
    gr1 = grade1 * "*"
    gr2 = grade2 * "*"
    gr3 = grade3 * "*"
    gr4 = grade4 * "*"
    gr5 = grade5 * "*"
    print("Statistics:")
    print(f"Points average: {average}")
    print(f"Pass percentage: {passP}")
    print(f"Grade distribution: ")
    print(f"5: {gr5}")
    print(f"4: {gr4}")
    print(f"3: {gr3}")
    print(f"2: {gr2}")
    print(f"1: {gr1}")
    print(f"0: {gr0}")






# caclulate excercise points
def exerPoints(exerNum):
    exPoints = exerNum // 10
    return exPoints


#get grade
def grades(points, excerPoints):
    grade = points + excerPoints
    if points < 10:
        return 0, grade
    elif grade < 15:
        return 0, grade
    elif grade < 18:
        return 1, grade
    elif grade < 21:
        return 2, grade
    elif grade < 24:
        return 3, grade
    elif grade < 28:
        return 4, grade
    else:
        return 5, grade

input_user()