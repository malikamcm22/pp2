import re


def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match(input()))



#final_list = re.findall(r".*a+.*", file.read())s