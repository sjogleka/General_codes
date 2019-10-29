def balancedOrNot(expressions, maxReplacements):
    return_array = []
    for i in range(0, len(maxReplacements)):
        return_array.append(0)

    for count, each_data in enumerate(expressions):
        check_str = expressions[count]
        replacement_count = 0

        continue_loop = True
        while len(check_str) >= 1 and continue_loop:
            opening_count = check_str.count('<')
            closing_count = check_str.count('>')

            if opening_count > closing_count:
                replacement_count = maxReplacements[count] + 1
                continue_loop = False
            elif check_str[0] == '>':
                replacement_count += 1
                check_str = check_str[1:]
            else:
                check_str = check_str.replace('<>', '')

        if replacement_count <= maxReplacements[count]:
            return_array[count] = 1

    return return_array


print(balancedOrNot(expressions=["<>", "<<><>>"], maxReplacements=[0, 0]))  # [1,0]
print(balancedOrNot(expressions=["<>>>", "<>>>>"], maxReplacements=[2, 2]))  # [1,0]
print(balancedOrNot(expressions=["<>", "<>><"], maxReplacements=[2, 2]))  # [1, 0]
print(balancedOrNot(expressions=["<<<>", "<<><><"], maxReplacements=[2, 2]))  # [0,0]

print(balancedOrNot(expressions=["<<<>>>", "<>"], maxReplacements=[2, 2]))  # [0,1]
print(balancedOrNot(expressions=["<<><>>", "<><>"], maxReplacements=[2, 2]))  # [0,1]

print(balancedOrNot(expressions=["<<><>><", "><><><"], maxReplacements=[2, 2]))  # [0,0]