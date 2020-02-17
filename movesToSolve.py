import heapq as heapq
import itertools
import collections


def movesToSolve(board):
    s = ''.join(str(d) for row in board for d in row)
    dq, seen = collections.deque(), {s}
    dq.append((s, s.index('0')))
    steps, height, width = 0, len(board), len(board[0])
    temp = ""
    for i in range(0,len(board[0])*len(board[1])):
        temp = temp+str(i)
    #print(t)
    while dq:
        for _ in range(len(dq)):
            t, i = dq.popleft()
            if t == temp:
                return steps
            x, y = i // width, i % width
            for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if height > r >= 0 <= c < width:
                    ch = [d for d in t]
                    ch[i], ch[r * width + c] = ch[r * width + c], '0'  # swap '0' and its neighbor.
                    s = ''.join(ch)
                    if s not in seen:
                        seen.add(s)
                        dq.append((s, r * width + c))
        steps += 1
    return -1

#print(movesToSolve([[1,6,3],[8,7,2],[4,0,5]]))
print(movesToSolve([[1,4,2],[3,0,5],[6,7,8]]))
print(movesToSolve([[1,0,2],[3,4,5],[6,7,8]]))
print(movesToSolve([[2,7,1],[6,3,5],[0,4,8]]))
print(movesToSolve([[0,4,2],[3,1,5],[6,7,8]]))