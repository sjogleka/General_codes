def strangeSort(mapping, nums):
    m = {}
    out = {}
    return_list = []
    for k, v in enumerate(mapping):
        m[v] = k
    for num in nums:
        number = 0
        for c in num:
            n = int(c)
            number = number * 10 + m[n]
        if number not in out:
            out[number] = []
        out[number].append(num)
    for each in sorted(out.keys()):
        for num in out[each]:
            return_list.append(num)
    print(return_list)

if __name__ == '__main__':
    mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
    nums = ['8', '12', '02', '4', '023', '65', '83', '224', '50']
    strangeSort(mapping,nums)