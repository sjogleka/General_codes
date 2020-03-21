'''from collections import Counter
def perseus_sort(l):
    counter = Counter(l)
    return sorted(l, key=lambda x: (counter[x], x))


li = [3,1,2,2,4]
print(perseus_sort(li))

'''
import heapq


def popularNToys(numToys, topToys, toys, numQuotes, quotes):
    toys_dict = {}
    for toy in toys:
        toys_dict[toy] = 0

    def toLower(quote):
        for c in quote:
            if not c.isalpha():
                quote = quote.replace(c, ' ')
        return quote.strip().lower()

    toys_count = {}
    toys_list = []

    for q in quotes:
        for word in set(toLower(q).split(' ')):
            if word in toys_dict:
                toys_dict[word] += 1

    for k, v in toys_dict.items():
        toys_list.append((-1 * v, k))

    heapq.heapify(toys_list)
    return [heapq.heappop(toys_list)[1] for x in range(topToys)]


print(popularNToys(6, 2, ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"], 6,
                   ["Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
                    "The new Elmo dolls are super high quality",
                    "Expect the Elsa dolls to be very popular this year",
                    "Elsa and Elmo are the toys I'll be buying for my kids",
                    "For parents of older kids, look into buying them a drone",
                    "Warcraft is slowly rising in popularity ahead of the holiday season"]))


[""]