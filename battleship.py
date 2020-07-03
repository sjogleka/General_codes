'''
def battleship(N, s, t):
    matrix = [[0] * N for _ in range(N)]

    ships = s.split(",")
    hits = t.split(" ")
    for i in range(len(ships)):
        ships[i] = ships[i].split(" ")
    print(ships)
    original = set()
    for i in range(len(ships)):
        top_left = ships[i][0].strip()
        bottom_right = ships[i][1].strip()
        print(top_left[:-1],top_left[-1])
        top_x = int(top_left[:-1]) - 1
        top_y = ord(top_left[-1]) - 65
        bottom_x = int(bottom_right[:-1]) - 1
        bottom_y = ord(bottom_right[-1]) - 65
        vertical = bottom_x - top_x + 1
        horizonal = bottom_y - top_y + 1
        for m in range(top_x, top_x + vertical):
            for n in range(top_y, top_y + horizonal):
                matrix[m][n] = i + 1
        original.add(i + 1)
        print(matrix)

    hitted = set()
    for hit in hits:
        x = int(hit[:-1]) - 1
        y = ord(hit[-1]) - 65
        if matrix[x][y] != 0:
            hitted.add(matrix[x][y])
            matrix[x][y] = 0

    updated = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                updated.add(matrix[i][j])

    sunk = len(original - updated)
    hitted_but_not_sunk = len(hitted & updated)

    return sunk, hitted_but_not_sunk
'''

def solution(N, S, T):
    sunk = 0
    hitsOfShips = 0
    result = ""
    battle= list()
    ships = S.split(",")
    for s in ships:
        cells = s.split(" ")
        cell = []
        for c in cells:
            char = 0
            row = ""
            column = ""
            while(c[char].isdigit()):
                row += c[char]
                char += 1
            column = c[char:]
            row = int(row) - 1
            column = ord(column) - ord("A")
            cell.append([row,column])
        battle.append(cell)
    print(battle)
    hits = set()
    t = T.split(" ")
    for hit in t:
        char = 0
        row = ""
        column = ""
        while hit[char].isdigit():
            row += hit[char]
            char += 1
        column = hit[char:]
        row = int(row) - 1
        column = ord(column) - ord("A")
        hits.add((row, column))

    print(hits)
    for s in battle:
        total = 0
        shipHits = 0
        for r in range(s[0][0], s[1][0]+1):
            for c in range(s[0][1],s[1][1]+1):
                if (r,c) in hits:
                    shipHits += 1
                total += 1
        if total == shipHits:
            sunk += 1
        elif shipHits > 0:
            hitsOfShips += 1

    result = ",".join([str(sunk),str(hitsOfShips)])
    return result

if __name__ == '__main__':
    '''
    N = 3
    S = "1A 1B,2C 2C"
    T = "1B"
    '''
    N = 4
    S = "1B 2C,2D 4D"
    T = "2B 2D 3D 4D 4A"
    #print(battleship(N,S,T))
    print(solution(N, S, T))