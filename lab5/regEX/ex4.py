import re
def text(a):
        x = '[A-Z]+[a-z]+$'
        if re.search(x,  a):
                return 'Yes'
        else:
                return('No')
print(text(input()))