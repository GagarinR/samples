s = '1-10,14, 20-25:2' #, 
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24])
'''

# def range_parser(string):
#     lst = string.split(',')
#     result = []
#     for single_range in lst:
#         single_range = single_range.strip()
#         if ('-' in single_range) and (':' not in single_range):
#             numbers = single_range.split('-')
#             result.extend([x for x in range(int(numbers[0]), int(numbers[1]) + 1)])
#         elif ('-' not in single_range) and (':' not in single_range):
#             result.append(int(single_range))
#         else:
#             numbers = single_range.split('-')
#             second_number = int(numbers[1].split(':')[0])
#             step = int(numbers[1].split(':')[1])
#             result.extend([x for x in range(int(numbers[0]),  second_number + 1, step)])
#     return result


# range_parser(s)




##################################
def range_parser(s):
    b,c =[],[]
    for i in s.split(','):
        print('====Current i: ', i)
        print('dash', i.count('-'))
        if i.count('-') == 0:
            b.append(i + '-' + i + ':1')
            

        else:
            print('in else. ":":', i.count(':'))
            if i.count(':')==0:
                b.append(i+':1')
            else:
                b.append(i)
        print('current b:', b)
    for i in b:
        t = (i.split(':'))
        t2 = (t[0].split('-'))
        for i2 in range(int(t2[0]),int(t2[1])+1, int(t[1])):
            c.append(i2)
    return c
range_parser(s)
