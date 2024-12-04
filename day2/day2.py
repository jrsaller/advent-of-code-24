import shared

lines = shared.read_file("source.txt")

def outside_range(x):
    return x > 3 or x < -3 or x == 0

def is_list_okay(arr):
    print("OG", arr)
    da = []
    for i in range(len(arr)-1):
        da.append(arr[i] - arr[i+1])
    print("diff",da)
    if list(filter(outside_range, da)):
        print("The diffs are too large or have a zero\n")
        return 0
    elif all(item > 0 for item in da) or all(item < 0 for item in da):
        print("FINAL SCORE + 1\n")
        return 1
    else:
        print("Not all items increase or decrease")
    print()
    return 0

total = 0
for line in lines:
    a = list(map(int,line.split()))
    total += is_list_okay(a)
    
        
print("PART 1 FINAL SCORE:", total, "\n\n\n")

t2 = 0
for line in lines:
    a = list(map(int,line.split()))
    res = is_list_okay(a)
    if res == 0:
        for i in range(len(a)):
            temp = a[:]
            temp.pop(i)
            res = is_list_okay(temp)
            if res == 1:
                t2 += 1
                break
    else:
        t2 += 1

print("PART 2 FINAL SCORE:", t2)