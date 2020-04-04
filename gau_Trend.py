import itertools


def solution(A, B, C, D):
    result = {}
    perms = itertools.permutations([A, B, C, D])
    for p in perms:
        if ((p[0] == 2 and p[1] <= 3) or p[0] <= 1) and p[2] <= 5:
            temp = str(p[0]) + str(p[1]) + str(p[2]) + str(p[3])
            result[int(temp)] = temp

    if result == {}:
        return "NOT POSSIBLE"

    m = result[max(result)]

    return m[:2] + ":" + m[2:]


if __name__ == '__main__':
    print(solution(2,4,0,0))
    print(solution(3, 0, 7, 0))