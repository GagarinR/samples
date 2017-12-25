# s1 = "apples, pears # and bananas\ngrapes\nbananas !apples"
s1 = "apples, pears\ngrapes\nbananas "
m1 = ["#", "!"]

def solution(string,markers):
    # print('original')
    # print( repr(string))
    string = string.strip()
    str1 = string.split("\n")
    # print(str1)

    for mark in markers:

        for ind, i in enumerate(str1):
            print(ind)
            if i.find(mark) != -1:

                str1.remove(i)
                str1.insert(ind,i[:i.find(mark)-1])
                # print i.strip(" ")
    # print(repr(str1))
    # for i in str1:
    #     print(''.join(i))
    #     if i.find(' ') != -1:
    #         print ("find space", i, i.find(' ') )


    return "\n".join(str1)###############################




print(repr(solution(s1,m1)))
