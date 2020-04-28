s = "d1/d2/a"
s1 = "a"
s2 = "d1/d2/b"
paths = [s,s1,s2]
ip_set = []
target = "d2"
op = []
'''
for i in range(len(paths)):
    # Making set of all directories in a paths by spliting on '/'
    ip_set.append(set(paths[i].split('/')))


for i in range(len(ip_set)):
    if target in ip_set[i]:
        op.append(paths[i])

print(op)
'''



import os
import sys

walk_dir = '.'

print('walk_dir = ' + walk_dir)
target_file = 'Akuna_Binary_wal.py'
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

res = []

def funcRec(walk_dir):
    for root, subdirs, files in os.walk(walk_dir):
        #print("....",walk_dir,"....",subdirs)
        if target_file in files:
            res.append(root)
        for i in subdirs:
            funcRec(i)
funcRec(walk_dir)
print(res)