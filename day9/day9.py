import shared

part1 = True

def first_non_negative(list, stop):
    for i in range(len(list)-1,stop,-1):
        if list[i] > 0:
            return i
    return -1

def first_negative(list,blockcount, stop):
    for i in range(stop):
        if list[i] == -1:
            if all(x == -1 for x in list[i:i+blockcount]):
                return i
    return -1

lines = shared.read_file("source.txt")

id = 0
file = True
s = []

for char in lines[0]:
    c = id if file else -1
    s.extend([c] * int(char))
    file = not file
    id += 1 if file else 0


if part1:
    i = 0
    while not all(x == -1 for x in s[len(s):-s.count(-1)-1:-1]):
        if s[i] == -1:
            swap = first_non_negative(s,i)
            s[i], s[swap] = s[swap], s[i]
        i += 1
else:
    for i in range(len(s)-1,0,-1):
        if s[i] != -1:
            blockcount = s.count(s[i])
            pos = s.index(s[i])
            swap = first_negative(s, blockcount,pos)
            if swap != -1:
                s[pos:pos+blockcount],s[swap:swap+blockcount] = s[swap:swap+blockcount],s[pos:pos+blockcount]

final_file = s[:len(s)-s.count(-1)]

total = 0
for x in range(len(s)):
    if s[x] != -1:
        total += x * s[x]
        print(total, x, s[x])
print(total)