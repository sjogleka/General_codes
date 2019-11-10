import re

def retrieveMostFrequentlyUseWords(literatureText, wordsToExclude):
    for i in range(len(wordsToExclude)):
        wordsToExclude[i] = wordsToExclude[i]

    print(wordsToExclude)
    wordsToExclude = set(wordsToExclude)
    words = {}
    for i in range(len(literatureText)):
      if literatureText[i] != " " and not literatureText[i].isalpha():
          literatureText[i] = " "
    inputStr = "".join(literatureText).lower()
    inputList = inputStr.split(" ")
    for word in inputList:
      if not word:
        continue
      if word not in wordsToExclude:
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1
    sorted_words = sorted(words.items(), key = lambda x: x[1], reverse=True)
    results = []
    max_count = float('-inf')
    for word, freq in sorted_words:
      if max_count <= freq:
        results.append(word)
        max_count = freq
      else:
        break
    return  results

def solution(sentence, stop_words):
    stop_words = [x.lower() for x in stop_words]
    res = re.findall(r'\w+', sentence)
    res = [x.lower() for x in res]

    worddict = {}

    for word in res:
        if word not in worddict:
            worddict[word] = 1
        else:
            worddict[word] += 1

    print(worddict)

    fwords = []
    for value in worddict:
        if (worddict[value] > 1) and (value not in stop_words):
            fwords.append(value)

    print(fwords)


if __name__ == '__main__':
    inputStr = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
    # inputStr = "Rose is a flower red rose are flower"
    stop_words = ["and", "he", "the", "to", "is", "Jack", "Jill"]
    # stop_words = set(['is', "are", "a"])
    inputStr = list(inputStr)
    #print(retrieveMostFrequentlyUseWords(inputStr,stop_words))
    solution(inputStr,stop_words)
#print(mostCommonWord("Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food",["and", "he", "the", "to", "is", "Jack", "Jill"]))