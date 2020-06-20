def solution(s,k):
    if k >= len(s):
        return s
    result = s[:k+1]
    if s[-1]==' ':
        return result
    while result[k]!=' ':
        k -=1
    return result[:k].strip()

if __name__ == '__main__':
    #given = "Codility we test coders"
    given = "The quick brown fox jumps over the lazy dog"
    #k_given = 14
    k_given = 100
    print(solution(given,k_given))

