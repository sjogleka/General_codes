from collections import Counter

str1 = input("Please enter a sentence: ")
words = str1.split(',')
print(words)
s = set()
for i in range(len(words)):
    s.add(words[i].lower())
print(s)
print(len(s))
#c = Counter(words)
#unique = [w for w in words if c[w] == 1]

#print("Unique words: ", unique)

