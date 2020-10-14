import re
def firstRepeatedWord(sentence):
    s = set()
    d = ",.:;-"
    temp = []
    sentence = re.split("["+"\\".join(d)+"]",sentence)
    for ele in sentence:
        if ele not in d:
            temp.extend(ele.split())
    for item in temp:
        if item not in s:
            s.add(item)
        else:
            return item

    return -1

print(firstRepeatedWord("We Work hard because hard work pays."))
print(firstRepeatedWord("He had had quite enough of this nonsense"))