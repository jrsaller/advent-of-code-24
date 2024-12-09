import shared

def r_math(acc,l, part2):
    # print(acc)
    # print(l)
    if not l:
        return acc
    n = l[0]
    ta = []
    for item in acc:
        ta.append(item + n)
        ta.append(item * n)
        if part2:
            ta.append(int(str(item) + str(n)))
    return r_math(ta, l[1:], part2)


lines = shared.read_file("source.txt")
p1 = 0
part2 = False

for line in lines:
    # print(line)
    goal, ops = line.split(":")
    goal = int(goal)
    nums = list(map(int,ops.split()))
    # print(goal)
    # print(nums)
    finals = r_math([nums[0]], nums[1:],part2)
    # print(finals)
    if goal in finals:
        # print("this line will work!")
        p1 += goal

print("answer:", p1)