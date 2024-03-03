st=input()
def count_upper_lower(string):
    upper_cnt = 0
    lower_cnt = 0
    
    for char in string:
        if char.isupper():
            upper_cnt += 1
        elif char.islower():
            lower_cnt += 1
    
    return upper_cnt, lower_cnt

print(count_upper_lower(st))
