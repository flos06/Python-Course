# Write your solution here
def find_movies(database: list, search_term: str):
    test = []
    for title in database:
        print(title["name"])
        if search_term in title["name"].lower():
            test.append(title)

    return test


