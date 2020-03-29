import collections
def subStringsWithKDistinctCharacters(s, k):
    s = list(s)
    count = 0
    right, left = 0, 0
    hmap = collections.defaultdict(int)
    for x in s:
        hmap[x] += 1

        if len(hmap) < k:
            continue

        if len(hmap) > k:
            del hmap[s[right]]
            right += 1
            left = right

        while hmap[s[right]] > 1:
            hmap[s[right]] -= 1
            right += 1
        count += right - left + 1
    return count

if __name__ == '__main__':
    print(subStringsWithKDistinctCharacters("abaca",2)