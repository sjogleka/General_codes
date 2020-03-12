import collections
def calculate_coffee_stats(office_stats_list):
    d = collections.defaultdict(dict)
    op = []
    for i in range(len(office_stats_list)):
        office_stats_list[i] = office_stats_list[i].replace("\r","")
        temp = office_stats_list[i].split(',')
        j = 0
        if temp[j] in d:
            d[temp[j]] [temp[j + 1]] = temp[j + 2]
        else:
            d[temp[j]] = {temp[j+1]:temp[j+2]}

    #print(d)
    for k,v in d.items():
        t = ""
        t+=k
        avg  =0
        for j,l in v.items():
            avg  = avg + int(l)
        t+=","+(str(avg))
        t+=","+(str(avg//len(v)))
        op.append(t)
    return op


if __name__ == '__main__':
    #l = ['Auc,Aug,9160','Auc,Jan,9160','Auc,Feb,9160']
    '''
    l = ['Auckland,Jan,9160','Auckland,Feb,5640', 'Auckland, Mar, 2323',
         'Auckland, Apr, 3214',
         'Auckland,May, 5645',
         'Auckland, Jun, 5678',
         'Auckland,Jul, 4175',
         'Auckland,Aug, 2020',
         'Auckland,Oct, 9823',
         'Auckland,Nov, 6540',
         'Auckland,Dec, 2563']
    '''

    l = ['Auckland, Jan, 9160',
         'Auckland, Feb, 5640',
         'Auckland, Mar, 2323',
         'Auckland, Apr, 3214',
         'Auckland, May, 5645',
         'Auckland, Jun, 5678',
         'Auckland, Jul, 4175',
         'Auckland, Aug, 2020',
         'Auckland, Oct, 9823',
         'Auckland, Nov, 6540',
         'Auckland, Dec, 2563',
         'Wellington, Jan, 5678',
         'Wellington, Feb, 4175',
         'Wellington, Mar, 2020',
         'Wellington, Apr, 9823',
         'Wellington, May, 6540',
         'Wellington, Jun, 2563',
         'Wellington, Jul, 9160',
         'Wellington, Aug, 5640',
         'Wellington, Oct, 2323',
         'Wellington, Nov, 3214',
         'Wellington, Dec, 5645']


print(calculate_coffee_stats(l))
