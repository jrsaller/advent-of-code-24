import shared
import functools
import sys
import os

rules, pages = open(os.path.join(sys.path[0],'source.txt')).read().split('\n\n')

rules = rules.split('\n')
pages = pages.split('\n')

def has_overlap(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return not s1.isdisjoint(s2)
    
d = dict()
badupdates = []
total = 0
total2 = 0
for r in rules:
    data = r.split("|")
    p0 = data[0]
    p1 = data[1]
    if p0 in d.keys():
        d[p0].append(p1)
    else:
        d[p0] = [p1]

# for item in d.keys():
#     print(item,d[item])


for p in pages:
    update = p.split(",")
    # print(update)
    bad_update = False
    for i in range(len(update)-1,0,-1):
        item = update[i]
        if item in d.keys():
            if has_overlap(d[item], update[:i]):
                bad_update = True
                break
    if bad_update:
        # print("mistake!!!!")
        badupdates.append(update)
    else:
        # print("THIS LINE WAS GOOD")
        total += int(update[len(update)//2])

print("part 1:", total)

cmp = functools.cmp_to_key(lambda x,y: 1-2*(x+'|'+y in rules))

total2=0
for update in badupdates:
    total2 += int(sorted(update,key=cmp)[len(update)//2])

print("part 2", total2)