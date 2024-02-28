import re
def text(a):
        x = 'ab{2,3}'
        if re.search(x,  a):
                return 'Yes'
        else:
                return('No')
        
print(text(input()))