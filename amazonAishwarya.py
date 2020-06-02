import collections
import heapq
import re

class Solution(object):
    def topKFrequentMentionedKeywords(self,numOfCompetitors,topNCompetitors ,competitors, numReviews,reviews):
        data_value_dict = collections.Counter()
        key_value_dict = set(competitors)
        for review in reviews:
            temp_list = review.lower().split(' ')
            for value in temp_list:
                value = re.sub('[^a-z]', '', value)
                #print(value)
                if value in key_value_dict:
                    data_value_dict[value] += 1
        res = heapq.nsmallest(topNCompetitors, data_value_dict, key=lambda x: (-data_value_dict[x], x))
        return res

def main():
    k = 8
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular."]

    competitors = ["newshop", "mymarket", "fashionbeats", "shopnow", "afshion", "tcellular"]
    reviews = ["newshop is providing good service in the city: Everyone should use newshop",
               "best service by newshop",
               "Fashionbeats has great service in the city",
               "I am proud to have Fashionbeats",
               "mymarket has awesome services",
               "Thanks Newshop for the quick delivery"]




    solution = Solution()
    #print(solution.topKFrequentMentionedKeywords(len(competitors), k, competitors, len(reviews), reviews))
    print(solution.topKFrequentMentionedKeywords(len(competitors),k,competitors,len(reviews),reviews))
    #res = solution.topKFrequentMentionedKeywords(keywords, reviews, k)

if __name__ == "__main__":
    main()