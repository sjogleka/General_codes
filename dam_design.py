
def wall(wallPositions,wallHeight):
    n = len(wallPositions)
    m = len(wallHeight)
    max_mud_len = -1
    for i in range(n - 1):
        if wallPositions[i] < wallPositions[i + 1] - 1:
            heightDiff = abs(wallHeight[i + 1] - wallHeight[i])
            gapLen = wallPositions[i + 1] - wallPositions[i] - 1
            if gapLen > heightDiff:
                low = max(wallHeight[i + 1], wallHeight[i]) + 1
                remainingGap = gapLen - heightDiff - 1
                localMax = low + remainingGap // 2
            else:
                localMax = min(wallHeight[i + 1], wallHeight[i]) + gapLen

            max_mud_len = max(max_mud_len, localMax)
    return max_mud_len
