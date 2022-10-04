# Write your solution here
def anagrams(str1, str2):
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'ollhe'
    print(anagrams(str1, str2))