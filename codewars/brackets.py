# Write a function that takes a string of braces, and determines if the order of the braces is valid.
#  It should return true if the string is valid, and false if it's invalid.
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


s1 = "(){}[]"
s2 = "([{}])"
s3 = "(}"
s4 = "[(])"
s5 = "[({})](]"


def braces_check(s):
    if type(s) != str or len(s) < 2:
        return s, False, "Length is <2 or type is not str"
    lst_s = list(s)
    closing_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'}
    indexes_of_open_and_closing = []
    for index, letter in enumerate(lst_s):
        # if we have closing bracket, let's look for the opening one and delete both
        if letter in closing_brackets.keys():
            previous_letter = s[index - 1]
            # If previous bracket is not opening bracket of current one
            # For example [), we return False.
            if previous_letter != closing_brackets[letter] and (previous_letter not in closing_brackets.keys()): 
                return s, False, 'Previous bracket of current closing bracket is not opening one'
            # let's find the closest opening bracket
            index_closest_opening = s[:index].rfind(closing_brackets[letter])
            # print( letter, "it's closing", index, "opening:", index_closest_opening)
            if index_closest_opening == -1: 
                return s, False, "We did not find any opening bracket"  # we haven't found any opening bracket for this closing one
            indexes_of_open_and_closing.append(index_closest_opening)
            indexes_of_open_and_closing.append(index)

    if len(indexes_of_open_and_closing) != len(s): # in case we have one bracket which doesn't have a pair, this would be unequal
        return s, False
    # print(lst_s)
    return s, True
print(braces_check(s1))
print(braces_check(s2))
print(braces_check(s3))
print(braces_check(s4))
print(braces_check(s5))
print(braces_check(")"))
print(braces_check(""))