def palindrome(string):
    return string == ''.join(reversed(string))

string = input()
if palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")