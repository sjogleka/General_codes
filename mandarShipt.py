import  requests
global res


public_api_key = "c582ea9a34cde7a37a2f25e9c2d7b220"
hash = "24d9cacc8dbd3893ac7d367d347a33af"
#hash = "24d9cacc8dbd3893ac7d367d37a33af" #Uncomment for negative testing
class CharacterFinder:

    def __init__(self,charName1,charName2=None):
        self.charName1 = charName1
        self.charName2 = charName2
        self.link = "https://gateway.marvel.com/v1/public/characters/"
        self.comics = self.getComicNames(self.charName1)

    def getComicNames(self,character):
        self.characterLink = self.link + str(res[character]) + "?ts=1234&apikey="+public_api_key+"&hash="+hash
        #Uncomment for negative testing
        #self.characterLink = self.link + str(res[character]) + "?ts=1234&apikey=c582ea9a4cde7a37a2f25e9c2d7b220&hash=24d9cacc8dbd3893ac7d367d347a33af"
        try:
            self.data_1 = requests.get(self.characterLink).json()['data']['results'][0]['comics']['items']
        except:
            print("Error in retriving the data from the API ! Please check URL you are hitting")
            exit(1)
        result_1 = set()
        for ele in  self.data_1:
            result_1.add(ele['name'])
        return result_1

    def checkCommon(self):
        op  = self.comics.intersection(self.getComicNames(self.charName2))
        return op if op else None

if __name__ == '__main__':
    res = {}
    result = []
    offset = "0"
    link1 = "https://gateway.marvel.com/v1/public/characters?offset="
    link2 = "&limit=100&ts=1234&apikey="+public_api_key+"&hash="+hash
    link = link1 + offset + link2
    try:
        result = requests.get(link).json()['data']['results']
    except:
        print("Error in retriving the data from the API ! Please check URL you are hitting")
        exit(1)
    while result:
        print("Retrieving Data from API ...")
        offset = str(int(offset) + 100)
        for ele in result:
            res[ele['name']] = ele['id']
        link = link1 + offset + link2
        result = requests.get(link).json()['data']['results']
    print("..........................................................")
    print("....................... Test Cases .......................")
    print("..........................................................")
    print("TestCase 1:")
    print("Characters used: - Iron Man, Captain America")
    ip1 = CharacterFinder('Iron Man','Captain America')
    finalResult = ip1.checkCommon()
    print("........ Final Result ..........")
    if finalResult:
        print("Common Comics are: - ")
        for ele in finalResult:
            print(ele)
    else:
        print("No Common Comic found")
    print("..."*20)
    print("TestCase 2:")
    print("Characters used: - Storm, Emma Frost")
    ip2 = CharacterFinder('Storm', 'Emma Frost')
    finalResult = ip2.checkCommon()
    print("........ Final Result ..........")
    if finalResult:
        print("Common Comics are: - ")
        for ele in finalResult:
            print(ele)
    else:
        print("No Common Comic found")

    print("..." * 20)
    print("TestCase 3:")
    try:
        ip3 = CharacterFinder()
    except:
        print("Error !!! Please provide atleast one character name")
