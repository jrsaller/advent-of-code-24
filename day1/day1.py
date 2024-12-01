import shared


lines = shared.read_file("source.txt")

col1 = []
col2 = []
for line in lines:
    data = line.split()
    col1.append(int(data[0]))
    col2.append(int(data[1]))

# print("OG1:", col1)
# print("OG2:", col2)
sort_col1 = sorted(col1)
sort_col2 = sorted(col2)
# print("SORT1:", sort_col1)
# print("SORT2:", sort_col2)

t=0
for i in range(len(sort_col1)):
    t += abs(sort_col1[i] - sort_col2[i])
# PART 1 ANSWER
print("PART 1:", t)

t2 = 0
for n in col1:
    # print(n, col2.count(n), n*col2.count(n))
    t2+= n*col2.count(n)

print("PART 2:", t2)