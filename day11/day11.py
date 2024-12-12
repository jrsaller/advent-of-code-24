import shared
import functools

from math import log10, floor

@functools.cache
def get_stone_result(num,blinks):
    if blinks == 0:
        return 1
    if num == 0:
        return get_stone_result(1,blinks-1)
    digits = floor(log10(num)) + 1
    if digits % 2:
        return get_stone_result(num * 2024, blinks-1)
    
    return get_stone_result(num // 10**(digits//2), blinks-1) + get_stone_result(num % 10**(digits//2), blinks-1)

def apply_rules(stones, blinks):
    total = 0
    for i in range(len(stones)):
        total += get_stone_result(stones[i], blinks)
    return total


lines = shared.read_file("source.txt")

stones = [int(x) for x in lines[0].split()]
blinks = 75

print("Initial arrangement:")
print(stones)
stones = apply_rules(stones, blinks)
print(stones, " Stones in place")