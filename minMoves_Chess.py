# Python3 code to find minimum steps to reach
# to specific cell in minimum moves by Knight
class cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x, y, N):
    if x >= 1 and x <= N and y >= 1 and y <= N:
        return True
    return False

def minMoves(n, startRow, startCol, endRow, endCol):
    startRow +=  1
    startCol += 1
    endRow += 1
    endCol += 1
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    queue.append(cell(startRow, endRow, 0))
    visited = [[False for i in range(N + 1)]for j in range(N + 1)]
    visited[startRow][endRow] = True
    while len(queue) > 0:
        t = queue[0]
        queue.pop(0)
        if (t.x == startCol and
                    t.y == endCol):
            return t.dist
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if isInside(x, y, N) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

if __name__ == '__main__':
    N = 9
    #knightpos = [6, 2]
    #targetpos = [1, 6]
    startRow = 4
    startCol = 4
    endRow = 4
    endCol = 8
    print(minMoves(N,startRow,startCol,endRow,endCol))

