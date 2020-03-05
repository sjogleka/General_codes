def validParanthesis(s):
    d  ={"(":")","[":"]","{":"}"}
    stack =[]

    for i in range(len(s)):
        if stack:
            if stack[-1] in d and d[stack[-1]]==s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if stack:
        return False
    return True


if __name__ == '__main__':
    print(validParanthesis("("))