import copy

def dfs(new_board,r,c,word,idx):
    if idx>= len(word):
        return  True

    if word[idx]!=new_board[r][c]:
        return False

    if r<0 or r>=len(new_board) or c<0 or c>=len(new_board[r]):
        return False
    new_board[r][c] = '-1'

    if dfs(new_board,r+1,c,word,idx+1) or dfs(new_board,r-1,c,word,idx+1) or dfs(new_board,r,c+1,word,idx+1) or dfs(new_board,r,c-1,word,idx+1):
        return True

    '''
    x = [1, -1, 0, 0]
    y = [0, 0, -1, 1]
    for m in range(4):
        new_r = r+x[m]
        new_c = c+y[m]
        if 0 <= new_r < len(new_board) and 0 <= new_c < len(new_board[0]):
            if dfs(new_board,new_r,new_c,word,idx+1) :
                return True
    '''

    new_board[r][c] = word[idx]

    return False

def findwords(board,words):
    res = []
    for i in range(len(words)):
        found = False
        new_board = copy.deepcopy(board)
        print(".......")
        print(words[i])
        print(".......")
        for j in range(len(board)):
            for k in range(len(board[0])):
                if dfs(new_board,j,k,words[i],0):
                    res.append(words[i])
                    found = True
            if found:
                break

    return res




if __name__ == '__main__':
    '''
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    
    board1 = [["a", "b"], ["c", "d"]]
    words1 = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]
    #expected = ["ab","ac","bd","ca","db"]

    board1 = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words1 = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
    '''
    board1 = [["a"]]
    words1 = ["a"]

    print(findwords(board1,words1))

