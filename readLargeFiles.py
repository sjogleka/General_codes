import pandas
from  operator import  itemgetter
cnt = 0
list1 = ['0', '1', '2','3','4','5','6','7','8','9']
'''
with open("data.txt",encoding="utf8",errors='ignore') as infile:

    for line in infile:
        cnt += 1
        #print(line.split())
        open('file%s.txt' % (cnt%10), 'a').write(line)
        print(cnt)
print(cnt)
'''
df_list = []
for ele in list1:
    print("Reading file", ele)
    with open('file%s.txt' % ele, encoding="utf8", errors='ignore') as infile:
        list2 = []
        for line in infile:
            line = line.split()
            if len(line)>=130:
                list2.append(line[:130])
                #list2.append((itemgetter(86,129)(line)))
            #list2.append(line)
        df_list.append(pandas.DataFrame(list2))
        print(df_list[int(ele)])
df = pandas.concat(df_list)
print("Created Dataframe .. ")
print(df)
df.to_csv('temp.csv')