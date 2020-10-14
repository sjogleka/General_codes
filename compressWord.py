def compressWord(word,k):
    res = []
    i = 0
    while i<len(word):
        if i+k-1<len(word):
            #print(word[i:i+k],str(word[i]*k))
            if word[i:i+k] == str(word[i]*k):
                temp = word[i]
                i = i + k
                #while word[i]==temp:
                #   i+=1

            else:
                res.append(word[i])
                i+=1
        else:
            res.append(word[i])
            i+=1

    #print(res)
    return("".join(res))


def compressWord_1(input, k):
    if not input:
        return input

    stack = []
    stack.append([input[0], 1])

    for i in range(1, len(input)):
        if input[i] != input[i - 1]:
            if stack[-1][1] >= k:
                while stack[-1][1] >= k:
                    stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])
        else:
            stack[-1][1] += 1

    while stack[-1][1] >= k:
        stack[-1][1] -= k
    if stack[-1][1] == 0:
        stack.pop()

    out = []
    for ltrs in stack:
        out += ltrs[0] * ltrs[1]

    print(''.join(out))
    return ''.join(out)

compressWord("aba",2)
compressWord("baac",2)
compressWord("aaac",2)
compressWord("aaac",3)
compressWord("abbcccb",3)

compressWord_1("aba",2)
compressWord_1("baac",2)
#candy_crush("aaac",2)
#candy_crush("aaac",3)
compressWord_1("abbcccb",3)
compressWord_1("zwppppppppppppppppmmmmmmmmmmpmsc",10)
