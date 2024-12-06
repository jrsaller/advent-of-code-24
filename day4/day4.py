import shared

lines = shared.read_file("source.txt")

LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1

def get_four_chars(ypos,xpos,ydir,xdir):
    s = lines[ypos][xpos]
    #right
    if ydir == 0 and xdir == RIGHT:
        if xpos + 3 >= len(lines[ypos]):
            return ""
        return lines[ypos][xpos:xpos+4]
    #down,right
    elif ydir == DOWN and xdir == RIGHT:
        if xpos + 3 >= len(lines[ypos]) or ypos + 3 >= len(lines):
            return ""
        s+=lines[ypos+1][xpos+1]
        s+=lines[ypos+2][xpos+2]
        s+=lines[ypos+3][xpos+3]
        return s
    #down
    elif ydir == DOWN and xdir == 0:
        if ypos + 3 >= len(lines):
            return ""
        s += lines[ypos+1][xpos]
        s += lines[ypos+2][xpos]
        s += lines[ypos+3][xpos]
    #down,left
    elif ydir == DOWN and xdir == LEFT:
        if xpos - 3 < 0 or ypos + 3 >= len(lines):
            return ""
        s += lines[ypos+1][xpos-1]
        s += lines[ypos+2][xpos-2]
        s += lines[ypos+3][xpos-3]
        
    #left
    elif ydir == 0 and xdir == LEFT:
        if xpos - 3 < 0:
            return ""
        s += lines[ypos][xpos-1]
        s += lines[ypos][xpos-2]
        s += lines[ypos][xpos-3]
    #up,left
    elif ydir == UP and xdir == LEFT:
        if xpos-3 < 0 or ypos-3 < 0:
            return ""
        s += lines[ypos-1][xpos-1]
        s += lines[ypos-2][xpos-2]
        s += lines[ypos-3][xpos-3]
    #up
    elif ydir == UP and xdir == 0:
        if ypos - 3 < 0:
            return ""
        s += lines[ypos-1][xpos]
        s += lines[ypos-2][xpos]
        s += lines[ypos-3][xpos]
    #up,right
    elif ydir == UP and xdir == RIGHT:
        if ypos - 3 < 0 or xpos + 3 >= len(lines[ypos]):
            return ""
        s += lines[ypos-1][xpos+1]
        s += lines[ypos-2][xpos+2]
        s += lines[ypos-3][xpos+3]
    else:
        print("Something is very wrong.....")
    return s

def check_box(ypos,xpos):
    if xpos-1 < 0 or xpos+1 >=len(lines[ypos]) or ypos -1 < 0 or ypos+1 >= len(lines):
        return False
    tl = lines[ypos-1][xpos-1]
    tr = lines[ypos-1][xpos+1]
    bl = lines[ypos+1][xpos-1]
    br = lines[ypos+1][xpos+1]
    if tl == "M" and tr == "M" and bl == "S" and br == "S":
        return True
    if tl == "M" and bl == "M" and tr == "S" and br == "S":
        return True
    if bl == "M" and br == "M" and tl == "S" and tr == "S":
        return True
    if tr == "M" and br == "M" and tl == "S" and bl == "S":
        return True
    return False

total = 0
total2 = 0
for l in range(len(lines)):
    for xpos in range(len(lines[l])):
        if lines[l][xpos] == "X":
            if get_four_chars(l,xpos,0,RIGHT) == "XMAS":
                # print(l,xpos, "RIGHT")
                total += 1
            if get_four_chars(l,xpos,DOWN,RIGHT) == "XMAS":
                # print(l,xpos, "DOWN RIGHT")
                total += 1
            if get_four_chars(l,xpos,DOWN,0) == "XMAS":
                # print(l,xpos, "DOWN")
                total += 1
            if get_four_chars(l,xpos,DOWN,LEFT) == "XMAS":
                # print(l,xpos, "DOWN LEFT")
                total += 1
            if get_four_chars(l,xpos,0,LEFT) == "XMAS":
                # print(l,xpos, "LEFT")
                total += 1
            if get_four_chars(l,xpos,UP,LEFT) == "XMAS":
                # print(l,xpos, "UP LEFT")
                total += 1
            if get_four_chars(l,xpos,UP,0) == "XMAS":
                # print(l,xpos, "UP")
                total += 1
            if get_four_chars(l,xpos,UP,RIGHT) == "XMAS":
                # print(l,xpos, "UP RIGHT")
                total += 1
        if lines[l][xpos] == "A":
            if check_box(l,xpos):
                total2 += 1
    # print()
print("total 1", total)
print("total 2", total2)