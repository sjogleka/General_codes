def solve(S):
    ans = set()
    N = len(S)
    for center in range(2*N - 1):
        print("...........")
        print(center)
        left = center // 2
        right = left + center % 2
        print(left,right)
        while 0 <= left and right < len(S) and S[left] == S[right] and left!=right:
            print(left,right)
            ans.add(S[left: right+1])
            left -= 1
            right += 1
    return sorted(ans)[0] if ans else None

def longestPalindrome(s):
    op = ''
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(op) >= j - i:
                break
            elif s[i:j] == s[i:j][::-1]:
                op = s[i:j]
                break
    return op


#print(solve("YABCCBAZ"))
#print(solve("MALAYALAM"))
#print(solve("AABB"))
#print(solve("ABC"))
print(longestPalindrome("AABB"))
print(longestPalindrome("AncyFtFyncA"))
print(longestPalindrome("0100100010010"))
print(longestPalindrome("0100100010010"))
