# Write your solution here

def oldest_person(people:list):
    oldest = people[0][1]
    name = ''
    for person in people:
  
        if person[1] <= oldest:
            
            oldest = person[1]
            name = person[0]
            print(name)
    return name



