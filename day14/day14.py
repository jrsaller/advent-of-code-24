import shared
import re

max_width = 101
max_height = 103



class Bot:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x += max_width
        if self.y < 0:
            self.y += max_height
        if self.x >= max_width:
            self.x -= max_width
        if self.y >= max_height:
            self.y -= max_height


lines = shared.read_file("source.txt")
q = [0] * 4
bots = []
for line in lines:
    x,y,dx,dy = map(int,re.findall(r'-?\d+', line))
    print(x,y,dx,dy)
    bots.append(Bot(x,y,dx,dy))
    x_final = ((100 * dx) + x) % max_width
    y_final = ((100 * dy) + y) % max_height
    print(x_final,y_final)
    mid_width = max_width // 2
    mid_height = max_height //2
    if x_final == mid_width :
        print("\tOn the middle vertical")
        continue
    if y_final == mid_height:
        print("\tOn the middle horizontal")
        continue
    if x_final < mid_width and y_final < mid_height:
        q[0] += 1
        print("\tQ1")
    elif x_final > mid_width and y_final < mid_height:
        q[1] += 1
        print("\tQ2")
    elif x_final < mid_width and y_final > mid_height:
        q[2] += 1
        print("\tQ3")
    elif x_final > mid_width and y_final > mid_height:
        q[3] += 1
        print("\tQ4")

print("Q", q)
total = 1
for num in q:
    total *= num

tick = 0
foundit = False
while foundit == False and tick < 1000000:
    display = [["."] * max_width for _ in range(max_height)] 
    for b in bots:
        display[b.y][b.x] = "*"
        b.move()

    for line in display:
        if "**********" in "".join(line):
            foundit = True
        # for char in line:
        #     print(char, end="")
        # print()
    print("Tick",tick)
    tick += 1

for line in display:
    for char in line:
        print(char, end="")
    print()
    

print("Part 1:", total)
print("Part 2", tick)
