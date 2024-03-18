import re
def text(a):
        x = '^[a-z]+_[a-z]+$'
        if re.search(x,  a):
                return 'Yes'
        else:
                return('No')
print(text(input()))