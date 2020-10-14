'''
def find_exit(board,row,column):
    visited = set()
    x = [-1,1,0,0]
    y = [0,0,-1,1]
    q= [(row,column)]
    visited.add((row,column))
    last_row = len(board)-1
    last_column = len(board[0])-1
    first_row = 0
    first_column = 0
    #print(last_column,last_row,first_row,first_column)
    while q:

        current = q.pop(0)
        #print(q, "current", current)
        if current not in visited:
            visited.add(current)
            if current[0]==last_row or current[0] ==first_row or current[1] == last_column or current[1] == first_column:
                return current
        for i in range(4):
            xi = current[0] + x[i]
            yj = current[1] + y[i]
            #print(xi,yj)
            if 0<=xi<len(board) and 0<=yj<len(board[0]) and board[xi][yj]!='+' and (xi,yj) not in visited:
                q.append((xi,yj))

    return [-1,-1]
'''


def find_exit(board, row, column):
    visited = set()
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    exit = []  ##CHANGE
    q = [(row, column, 0)]  ##CHANGE
    max_level = 0  ##CHANGE
    visited.add((row, column))
    last_row = len(board) - 1
    last_column = len(board[0]) - 1
    first_row = 0
    first_column = 0
    while q:
        row, column, level = q.pop(0)  ##CHANGE
        current = (row, column)  ##CHANGE

        if level != max_level:  ##CHANGE TILL NEXT IF
            if exit:
                min_row = float("inf")
                min_col = float("inf")
                current = (-1, -1)
                for each in exit:
                    if each[0] == min_row:
                        if each[1] < min_col:
                            min_col = each[1]
                            current = (min_row, min_col)
                    if each[0] < min_row:
                        min_row = each[0]
                        min_col = each[1]
                        current = (min_row, min_col)
                return current

            max_level = level

        if current not in visited:
            visited.add(current)
            if current[0] == last_row or current[0] == first_row or current[1] == last_column or current[
                1] == first_column:
                exit.append(current)  ##CHANGE
        for i in range(4):
            xi = current[0] + x[i]
            yj = current[1] + y[i]
            if 0 <= xi < len(board) and 0 <= yj < len(board[0]) and board[xi][yj] != '+' and (xi, yj) not in visited:
                q.append((xi, yj, level + 1))  ##CHANGE

    if exit:
        min_row = float("inf")
        min_col = float("inf")
        current = (-1, -1)
        for each in exit:
            if each[0] == min_row:
                if each[1] < min_col:
                    min_col = each[1]
                    current = (min_row, min_col)
            if each[0] < min_row:
                min_row = each[0]
                min_col = each[1]
                current = (min_row, min_col)
        return current

    return (-1, -1)
#board = [['+', 0, 0, 0, '+'],['+', 0, '+', 0, '+'],['+', 0, 0, 0, '+'],['+', 0, '+', 0, '+']]
#board = [['+', '0', '+', '0', '+'],['0', '0', '0', '0', '0'],['+','+', '+', '+', '+'],['0', 0, '0', 0, '0'],['+', 0, '+', 0, '+']]
#board = [['+', '0', '+', '0', '+'],['0', '0', '+', '0', '0'],['+', '0', '+', '0', '+'],['0', '0', '+', '0', '0'],['+', '0', '+', '0', '+']]
#board = [['+','+','+','+','+','+'],['0','0','0','+','0','+'],['+','0','+','0','0','0'],['+','+','+','+','+','+']]

board = [['+','+','+','+','+','+','+','0','0'],
         ['+','+','0','0','0','0','0','+','+'],
         ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
         ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
         ['+','+','0','0','0','0','0','0','+'],
         ['+','+','0','+','+','0','+','0','+']]

#board  = [[]]
#print(find_exit(board,3,1))
#print(find_exit(board,0,1))
#print(find_exit(board,3,4))
#print(find_exit(board,3,0))
#print(find_exit(board,1,4))
#print(find_exit(board,1,0))
#print(find_exit(board,4,3))
#print(find_exit(board,0,3))
#print(find_exit(board,4,1))
#print(find_exit(board,0,1))
#print(find_exit(board,2,5))
#print(find_exit(board,1,0))
#print(find_exit(board,5,5))
#print(find_exit(board,5,2))
print(find_exit(board,0,7))
#print(find_exit(board,2,0))
#print(find_exit(board,8,8))