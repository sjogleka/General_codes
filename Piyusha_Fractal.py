def minimum_jumps(k,j):
    min_jumps = k/j
    min_jumps+=k%j
    #print(int(min_jumps))
    return int(min_jumps)

def missingWords(s,t):
    s = s.split()
    t = t.split()
    length = len(s)
    for i in reversed(s):
        if i in t:
            print(i)
            temp=i
            s.remove(temp)
            t.remove(temp)
            #i-=1
    print(s)

if __name__ == '__main__':
    print(minimum_jumps(3,1))
    print(minimum_jumps(8,3))
    print(minimum_jumps(3,3))

    #missingWords("Sumedh Joglekar","Sumedh")
    #missingWords("I am am using HackerRank to improve programming", "am HackerRank to improve")
    missingWords("Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming python elegant syntax and dynamic typing","Python is an easy to learn powerful programming language")
