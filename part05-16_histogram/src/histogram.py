# Write your solution here
def histogram(word: str):
    letter = {}
    for char in word:
        if char not in letter:
            letter[char] = 0
        letter[char] += 1
    for key, value in letter.items():
        print(f"{key} {value * '*'}")



