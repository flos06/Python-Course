# Write your solution here
def add_student(database, name):
    database[name] = ''
    return database

    

def print_student(database, name):

    if name in database:
        print(f"{name}:")
        if database[name] == '':
            print(f" no completed courses")
        else:
            average = 0
            print(f" {len(database[name])} completed courses:")
            for key, value in database[name]:
                print(f"  {key} {value}")
                average += value
            print(f" average grade {average / len(database[name])}")
    else:
        print(f"{name}: no such person in the database")

def add_course(database, name, course: tuple):
    test = []
    list_tuple = []


    if database[name] == "no completed courses" or database[name] == "": 
        database[name] = []
    database[name].append(tuple(course))



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")