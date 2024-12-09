import shared
import re

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

lines = shared.read_file("test_source.txt")

def on_map(lines, pos):
    y,x = pos
    if y < 0 or y >= len(lines):
        return False
    elif x < 0 or x >= len(lines[0]):
        return False
    return True



blocks = []
visited = [[] for _ in range(len(lines))]
vd = [["." for _ in range(len(lines[0]))] for _ in range(len(lines))]
loopstarters = 0
print(visited)

pos= (-1,-1)
face = NORTH

for i in range(len(lines)):
    blocks.append([match.start() for match in re.finditer("#", lines[i])])
    if "^" in lines[i]:
        pos = (i, lines[i].find("^"))

print(blocks)


while on_map(lines, pos):
    y = pos[0]
    x = pos[1]
    newpos = False
    if x not in visited[y]:
        visited[y].append(x)
        vd[y][x] = face
    else:
        od = vd[y][x]
        if face == NORTH and od == EAST:
            loopstarters+=1
        elif face == EAST and od == SOUTH:
            loopstarters+=1
        elif face == SOUTH and od == WEST:
            loopstarters+=1
        elif face == WEST and od == NORTH:
            loopstarters+=1
        
    # check y-1, x
    if face == NORTH:
        if y-1 < 0 or not x in blocks[y-1]:
            pos = (y-1,x)
            continue
        else:
            face = EAST
            pos = (y,x+1)
    # check y, x+1
    elif face == EAST:
        if x+1 > len(lines[y]) or not x+1 in blocks[y]:
            pos = (y,x+1)
            continue
        else:
            face = SOUTH
            pos = (y+1, x)
    # check y+1, x
    elif face == SOUTH:
        if y+1 >= len(blocks) or not x in blocks[y+1]:
            pos = (y+1, x)
            continue
        else:
            face = WEST
            pos = (y,x-1)
    # check y,x-1
    elif face == WEST:
        if x-1 < 0 or not x-1 in blocks[y]:
            pos = (y,x-1)
            continue
        else:
            face = NORTH
            pos = (y-1,x)
    else:
        print("Uh... how did you get here?")

total_visits = 0
print(visited)
for row in visited:
    total_visits += len(row)
for row in vd:
    for char in row:
        print(str(char) + "  ", end = "")
    print()

print("PART 1", total_visits)
print("PART 2", loopstarters)