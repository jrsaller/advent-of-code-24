import shared

lines = shared.read_file("source.txt")

map = shared.Grid(lines, int)

paths = 0

def search_grid(x, y, visited):
    total = 0
    point = map.get_point(x,y)
    if point == 9:
        global paths
        paths += 1
        if (x,y) in visited:
            return 0
        else:
            visited.append((x,y))
            return 1
    # NORTH
    np = map.get_point(x,y-1)
    if np == point + 1:
        total += search_grid(x,y-1, visited)
    # EAST
    ep = map.get_point(x+1,y)
    if ep == point + 1:
        total += search_grid(x+1,y, visited)
    # SOUTH
    sp = map.get_point(x,y+1)
    if sp == point + 1:
        total += search_grid(x,y+1, visited)
    # WEST
    wp = map.get_point(x-1,y)
    if wp == point + 1:
        total += search_grid(x-1,y, visited)
    return total

total = 0
paths = 0
for line in range(len(map.grid)):
    print(map.grid[line])
    for point in range(len(map.grid[line])):
        if map.get_point(point,line) == 0:
            total += search_grid(point,line, [])
print("PART 1:", total)
print("PART 2:", paths)