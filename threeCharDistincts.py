def threeCharDistincts(s):
    count = 0
    for i in range(len(s) - 2):
        #print(s[i])
        char_set = set()
        flag = True
        for j in range(i, i + 3):
            if s[j] in char_set:
                flag = False
                break
            else:
                char_set.add(s[j])

        if flag:
            count += 1
    return count

print(threeCharDistincts("aaaaaaabc"))
print(threeCharDistincts("abcdaaae"))