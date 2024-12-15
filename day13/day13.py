import shared
import re

lines = shared.read_file("source.txt")

part2 = True

acost = 3
bcost = 1

numbers = [int(num) for line in lines for num in re.findall(r'\d+', line)]

total = 0

for i in range(0,len(numbers),6):
    ax,ay,bx,by,winx,winy = numbers[i:i+6]
    if part2:
        winx += 10000000000000
        winy += 10000000000000
    print(ax,ay,bx,by,winx,winy)
    det_og = (ax * by) - (ay * bx)
    asol = (winx * by) - (winy * bx)
    asol /= det_og
    print("A:", asol)
    print(asol.is_integer())
    bsol = (ax * winy) - (ay * winx)
    bsol /= det_og
    print("B:", bsol)
    print(bsol.is_integer())
    if asol.is_integer() and bsol.is_integer():
        if not part2 and asol < 100 and bsol < 100:
            total += (asol * acost) + (bsol * bcost)
        elif part2:
            total += (asol * acost) + (bsol * bcost)
    print()

print(total)
    

