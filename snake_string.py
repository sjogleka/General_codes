### Print String sinusoidally ######
'''

e.g
 S = Hello_World


    E               _               L           ------------- 1st row
H       L       O       W       R       D       ------------- 2nd row
            L               O                   ------------- 3rd row

op = E_LHLOWRDLO

By Observation:-
1st row index = S[1],S[5] -- diff = 4
2nd row index = S[0], S[2], S[4],S[6] -- diff = 2
3rd row index = S[3],S[7] -- diff = 4
'''

def snake_string(s):
    op =[]
    if len(s)<=1:
        return s

    for i in range(1,len(s),4):
        op.append(s[i])

    for i in range(0,len(s),2):
        op.append(s[i])

    for i in range(3,len(s),4):
        op.append(s[i])

    return "".join(op)

def snake_string_1(s):

    return s[1::4]+s[::2]+s[3::4]
if __name__ == '__main__':
    print(snake_string("Hello_World"))
    print(snake_string_1("Hello_World"))