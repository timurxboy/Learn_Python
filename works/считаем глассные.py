def count_vowels(s):
    count = 0
    for i in s:
        if i in ['e','u','i','o','a']:
            count+=1
    
    return count