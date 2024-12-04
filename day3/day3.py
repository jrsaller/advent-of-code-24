import shared
import re

lines = shared.read_file("source.txt")

total1 = 0
total2 = 0
enabled = True
for line in lines:
    dos = re.finditer(r"do\(\)", line)
    do_index = [("do", do.start()) for do in dos]
    donts = re.finditer(r"don\'t\(\)", line)
    dont_index = [("dont", dont.start()) for dont in donts]
    muls = re.finditer(r"mul\(\d+,\d+\)", line)
    muls_index = [(mul[0], mul.start()) for mul in muls]
    muls = re.finditer(r"mul\(\d+,\d+\)", line)

    final = do_index + dont_index + muls_index
    final = sorted(final, key=lambda x: x[1])
    
    for cmd in muls:
        s = cmd[0].split(",")
        start = cmd.start()
        d1 = int(s[0].lstrip("mul("))
        d2 = int(s[1].rstrip(")"))
        total1 += (d1 * d2)
    
    for item in final:
        if item[0] == "dont":
            enabled = False
        elif item[0] == "do":
            enabled = True
        else:
            s = item[0].split(",")
            d1 = int(s[0].lstrip("mul("))
            d2 = int(s[1].rstrip(")"))
            if enabled:
                total2 += (d1 * d2)

print("PART 1: ", total1)
print("PART 2: ", total2)