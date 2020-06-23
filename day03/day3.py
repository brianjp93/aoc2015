"""day3.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

DIRS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


class Sled:
    def __init__(self, instructions):
        self.instructions = instructions
        self.coord = (0, 0)
        self.visited = {self.coord: 1}
        self.process()

    def process(self):
        for c in self.instructions:
            self.coord = tuple(a + b for a, b in zip(self.coord, DIRS[c]))
            self.visited[self.coord] = self.visited.get(self.coord, 0) + 1


class Robo:
    def __init__(self, instructions):
        self.instructions = instructions
        self.sleds = [(0, 0), (0, 0)]
        self.visited = {(0, 0): 1}
        self.process()

    def process(self):
        for i, c in enumerate(self.instructions):
            self.sleds[i % 2] = tuple(a + b for a, b in zip(self.sleds[i % 2], DIRS[c]))
            self.visited[self.sleds[i % 2]] = self.visited.get(self.sleds[i % 2], 0) + 1


with open(dpath) as f:
    data = f.read().strip()
    sled = Sled(data)
    print(len(sled.visited))

    robosled = Robo(data)
    print(len(robosled.visited))
