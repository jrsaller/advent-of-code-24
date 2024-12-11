import os
import sys

def read_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]
    
class Grid:
    def __init__(self,lines, cast=str):
        self.grid = []
        for line in lines:
            l = []
            for char in line:
                l.append(cast(char))
            self.grid.append(l)

    def get_point(self,x,y):
        if y < 0 or y >= len(self.grid) or x < 0 or x>=len(self.grid[0]):
            return -1
        return self.grid[y][x]
