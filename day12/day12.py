import shared
lines = shared.read_file("source.txt")
map = shared.Grid(lines)

regions = dict()
regionmap = [[-1] * len(map.grid[0]) for _ in range(len(map.grid))] 

def floodfill(x,y,regionnum):
    q = [(x,y)]
    area = 0
    while q:
        c,l = q.pop(0)
        area += 1
        char = map.get_point(c,l)
        regionmap[l][c] = regionnum
        #NORTH
        if map.get_point(c, l-1) == char and regionmap[l-1][c] == -1:
            if (c,l-1) not in q:
                q.append((c, l-1))

        #EAST
        if map.get_point(c+1, l) == char and regionmap[l][c+1] == -1:
            if (c+1,l) not in q:
                q.append((c+1, l))

        #SOUTH
        if map.get_point(c, l+1) == char  and regionmap[l+1][c] == -1:
            if (c, l+1) not in q:
                q.append((c, l+1))

        #WEST
        if map.get_point(c-1, l) == char  and regionmap[l][c-1] == -1:
            if (c-1, l) not in q:
                q.append((c-1, l))
    return area

regioncounter = 1
for l in range(len(map.grid)):
    for c in range(len(map.grid[l])):
        char = map.get_point(c,l)
        if regionmap[l][c] == -1:
            key = char+str(regioncounter)
        else:
            key = char + str(regionmap[l][c])
        if regionmap[l][c] == -1:
            a = floodfill(c,l, regioncounter)
            regioncounter+=1
        walls = 0
        corners = 0
        n = map.get_point(c,l-1)
        e =map.get_point(c+1,l) 
        s = map.get_point(c,l+1)
        w = map.get_point(c-1,l)
        nw = map.get_point(c-1,l-1)
        ne = map.get_point(c+1,l-1)
        se = map.get_point(c+1,l+1)
        sw = map.get_point(c-1,l+1)
        
        # NORTH
        if n != char:
            walls += 1
        # EAST
        if e != char:
            walls += 1
        # SOUTH
        if s != char:
            walls += 1
        # WEST
        if w != char:
            walls += 1


        # NORTH AND WEST
        if n == char and w == char and nw != char:
            corners += 1
        if n != char and w != char:
            corners += 1
        # NORTH AND EAST
        if n == char and e == char and ne != char:
            corners += 1
        if n != char and e != char:
            corners += 1
        # EAST AND SOUTH
        if e == char and s == char and se != char:
            corners += 1
        if e != char and s != char:
            corners += 1
        # SOUTH AND WEST
        if s == char and w == char and sw != char:
            corners += 1
        if s != char and w != char:
            corners += 1

        if key in regions.keys():
            regions[key]["perimeter"] += walls
            regions[key]["corners"] += corners
        else:
            regions[key] = {"perimeter": walls, "area" : a, "corners": corners}

total = 0
total2 = 0

for key in regions.keys():
    print(key, regions[key])
    total += regions[key]["perimeter"] * regions[key]["area"]
    total2 += regions[key]["corners"] * regions[key]["area"]

print("Part 1:",total)
print("Part 2:",total2)