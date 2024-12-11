import shared

lines = shared.read_file("source.txt")

part1 = False

MAX_R = len(lines)
MAX_C = len(lines[0])

d = dict()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        char = lines[r][c]

        if char != ".":
            if char not in d.keys():
                d[char] = [(r,c)]
            else:
                d[char].append((r,c))

hit_dict = dict()
for key in d.keys():
    print(key,d[key])
    for i in range(len(d[key])):
        item1 = d[key][i]
        for j in range(i+1, len(d[key])):
            item2 = d[key][j]
            r_dist = item1[0] - item2[0]
            c_dist = item1[1] - item2[1]
            new_point1 = (item1[0] + r_dist, item1[1] + c_dist)
            new_point2 = (item2[0] - r_dist, item2[1] - c_dist)
            print(new_point1, new_point2)
            if part1:
                if new_point1[0] >= 0 and new_point1[0] < MAX_R and new_point1[1] >= 0 and new_point1[1] < MAX_C:
                    print("HIT", new_point1)
                    if new_point1 not in hit_dict.keys():
                        hit_dict[new_point1] = 1
                    else:
                        hit_dict[new_point1] += 1
                if new_point2[0] >= 0 and new_point2[0] < MAX_R and new_point2[1] >= 0 and new_point2[1] < MAX_C:
                    print("HIT", new_point2)
                    if new_point2 not in hit_dict.keys():
                        hit_dict[new_point2] = 1
                    else:
                        hit_dict[new_point2] += 1
            else:
                if item1 in hit_dict.keys():
                    hit_dict[item1] +=1
                else:
                    hit_dict[item1] = 1
                if item2 in hit_dict.keys():
                    hit_dict[item2] +=1
                else:
                    hit_dict[item2] = 1

                while new_point1[0] >= 0 and new_point1[0] < MAX_R and new_point1[1] >= 0 and new_point1[1] < MAX_C:
                    print("HIT", new_point1)
                    if new_point1 not in hit_dict.keys():
                        hit_dict[new_point1] = 1
                    else:
                        hit_dict[new_point1] += 1
                    new_point1 = (new_point1[0] + r_dist, new_point1[1] + c_dist)
                while new_point2[0] >= 0 and new_point2[0] < MAX_R and new_point2[1] >= 0 and new_point2[1] < MAX_C:
                    print("HIT", new_point2)
                    if new_point2 not in hit_dict.keys():
                        hit_dict[new_point2] = 1
                    else:
                        hit_dict[new_point2] += 1
                    new_point2 = (new_point2[0] - r_dist, new_point2[1] - c_dist)
                    


print("total hits:", len(hit_dict.keys()))
print(hit_dict)