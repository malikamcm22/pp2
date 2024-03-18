import re
def text(a):
        x = 'a.*?b$'
        if re.search(x,  a):
                return 'Yes'
        else:
                return('No')
print(text(input()))