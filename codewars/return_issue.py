"""
Task
Given two cells on the standard chess board, determine whether they have the same color or not.

Example
For cell1 = "A1" and cell2 = "C3", the output should be true.
"""

def chess_board_cell_color(cell1, cell2):
    c = lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4').replace('E','5').replace('F','6').replace('G','7').replace('H','8')

    print(cell1, cell2)
    print(c(cell1), c(cell2))
    print(type(c))
    print(c('A1'))
    print(sum([int(i) for i in list(c('A1'))]))
    f1 = sum([int(i) for i in list(c(cell1))]) % 2 == 0
    f2 = sum([int(i) for i in list(c(cell2))]) % 2 == 0

    print(f1,f2)


    # return f1 == f2 
    
    ################################## return with True/False args doesnt work here!
    return (sum([int(i) for i in list(c(cell1))])%2 == 0) == (sum([int(i) for i in list(c(cell2))]) % 2 == 0)
    ########################################################################################################
print(chess_board_cell_color('H5','A4')) # True
