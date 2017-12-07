
s1 = "(){}[]"
s2 = "([{}])"
s3 = "(}"
s4 = "[(])"
s5 = "[({})]((]"

def validBraces(string):
    lst = ['()','{}','[]']
    for i in range(len(string)-1):
        braces = string[i]+ string[i+1]
        if braces in lst:
              return validBraces(string[:i]+string[i+2:])
    return not string

print (validBraces(s5))
