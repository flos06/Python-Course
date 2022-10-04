# write your solution here
from distutils.log import debug


def main():
    names = {}

        
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

    

    with open(student_info) as studentFile:
        for line in studentFile:
            parts = line.split(';')
            
            if parts[0] == 'id':
                continue
            
            names[parts[0]] = parts[1].strip() + ' ' + parts[2].strip()
    grades = {}
    with open(exercise_data) as gradeFile:
        for line in gradeFile:
            sum = 0
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            for i in range(1, len(parts)):
                sum += int(parts[i])
            grades[parts[0]] = sum

    for pic, name in names.items():
        if pic in grades:
            grade = grades[pic]
            print(f"{name} {grade}")


main()