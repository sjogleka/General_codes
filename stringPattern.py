##### 2/13 Passes  not consider one condition - > alternate vowels###
def calculateWays(wordlen,maxVowels):
    if maxVowels==0:
        ways = 1
        for i in range(wordlen):
            ways=ways*21
        return ways
    else:
        if wordlen==1:
            c,v=1,1
            ways= c*21 + v*5
            return ways
        else:
            ways =0
            for i in range(wordlen):
                print("i ->",i)
                c, v = 1, 1
                for j in range(wordlen-maxVowels):
                    print("j",j)
                    c=c*21
                for k in range(maxVowels):
                    v =v*5

                ways = ways+(v*c)

            ways1 = 1
            for i in range(wordlen):
                ways1  = ways1*21

            return ways1+ways


if __name__ == '__main__':
    print(calculateWays(1,1))
    print(calculateWays(4, 1))
    print(calculateWays(2, 1))

