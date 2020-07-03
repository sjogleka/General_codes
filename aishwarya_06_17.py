import math
def teamFormation(skills, minPlayers, minLevel, maxLevel):
    temp = []
    total = 0
    for ele in skills:
        if minLevel<=ele<=maxLevel:
            temp.append(ele)
    if len(temp)<minPlayers:
        return 0


    while minPlayers<=len(temp):
        total+=math.factorial(len(temp)) // (math.factorial(minPlayers) * math.factorial(len(temp)-minPlayers))
        minPlayers+=1
    return total


if __name__ == '__main__':
    skills = [12,4,6,13,5,10]
    #skills = [4,8,5,6]
    minPlayer = 3
    #minPlayer = 1
    minLevel = 4
    #minLevel = 5
    maxLevel = 10
    #maxLevel = 7

    print(teamFormation(skills,minPlayer,minLevel,maxLevel))