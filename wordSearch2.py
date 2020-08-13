'''
def searchWord(board,words):
    print(board,words)
    def backtrack(i, j, board, w, trie, res):
        if 'end' in trie:
            res.add(w)
            return True #Change
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] in trie:
            x = [1, -1, 0, 0]
            y = [0, 0, 1, -1]
            tmp = board[i][j]
            ret = False #Change
            board[i][j] = -1
            for n in range(4):
                ret  = backtrack(i + x[n], j + y[n], board, w + tmp, trie[tmp], res)
                if ret: #Change
                    return True#Change
            board[i][j] = tmp

    trie = {}
    output = []
    for word in words:
        t = trie
        for ele in word:
            if ele not in t:
                t[ele] = {}
            t = t[ele]
        t['end'] = '#'
        # print(trie)
    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            backtrack(i, j, board, '', trie, res)
    result = ""
    for ele in range(len(words)-1):
        if words[ele] in res:
            result +="Yes "
            #print("Yes ",end="")
        else:
            result += "No "
            #print("No ",end="")

    if words[-1] in res:
        result+="Yes"
        #print("Yes")
    else:
        result+="No"
        #print("No")
    print(result)
    #return output

size = input()
board= []
for i in range(int(size)):
    board.append(input().split())
print(board)
words = input().split()
searchWord(board,words)
#words = ["CAT","TOM","ADO","MOM","CDM"]
'''
'''
input -
3
M O M
S O N
R A T
MNT RAH MSR OOB
'''
#words = "MNT RAH MSR OOB"


def Wordsearch(board,word):
    vis = set()
    n, m = len(board), len(board[0])
    def word_exists(row, col, p):
        if p == len(word):
            return True

        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ci, cj = i + row, j + col
            if 0 <= ci < n and 0 <= cj < m and (ci, cj) not in vis and board[ci][cj] == word[p]:
                vis.add((ci, cj))
                if word_exists(ci, cj, p + 1):
                    return True

                vis.remove((ci, cj))

        return False


    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                vis.add((i, j))
                if word_exists(i, j, 1):
                    return True
                vis.remove((i, j))

    return False

size = input()
board= []
for i in range(int(size)):
    board.append(input().split())
if not board:
    print()
print(board)
words = input().split()
result = ""
for i in range(len(words)):
    if Wordsearch(board, words[i]):
        result +="Yes "
    else:
        result+="No "
print(result[:-1])
