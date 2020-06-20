def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1


def find_str1(full, sub):
    index = 0
    sub_index = 0
    position = -1
    for ch_i,ch_f in enumerate(full) :
        if ch_f.lower() != sub[sub_index].lower():
            position = -1
            sub_index = 0
        if ch_f.lower() == sub[sub_index].lower():
            if sub_index == 0 :
                position = ch_i

            if (len(sub) - 1) <= sub_index :
                break
            else:
                sub_index += 1

    return position

print(find_str("Happy birthday", "py"))

print(find_str1("Happy birthday", "py"))

#print(find_str("Happy birthday", "rth"))
#print(find_str("Happy birthday", "rh"))
