import os
import sys

def read_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]
    
class Grid:
    def __init__(self,lines,cast=str):
        self.grid = []
        for line in lines:
            l = []
            for char in line:
                l.append(cast(char))
            self.grid.append(l)

