# https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040/solutions/python

s1 = ')()('
s2 = ')('


def solve(s):
    if len(s) % 2 != 0:
        return -1
    stack = []
    for bracket in s:
        # print('Stack: ', stack)
        if bracket == ')' and len(stack) != 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    print('final stack: ', stack)
    stack_len = len(stack)
    n = 0
    while len(stack) != 0 and stack[-1] == '(':
        stack.pop()
        n += 1
    return (stack_len / 2 + n % 2)


print(solve(s2))
