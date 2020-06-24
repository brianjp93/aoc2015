"""day6.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")


class Yard:
    def __init__(self, instructions):
        self.instructions = instructions
        self.map = {}
        self.process()

    def process(self):
        for instr, start, end in self.instructions:
            self.do_instr(instr, start, end)

    def do_instr(self, instr, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if instr == "turn on":
                    self.map[(x, y)] = 1
                elif instr == "turn off":
                    self.map[(x, y)] = -1
                elif instr == "toggle":
                    self.map[(x, y)] = self.map.get((x, y), -1) * -1
                else:
                    print(instr)
                    print("instr not found")


class YardV2(Yard):
    def do_instr(self, instr, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                coord = (x, y)
                if instr == "turn on":
                    self.map[coord] = self.map.get(coord, 0) + 1
                elif instr == "turn off":
                    self.map[coord] = self.map.get(coord, 0) - 1
                    if self.map[coord] < 0:
                        self.map[coord] = 0
                elif instr == "toggle":
                    self.map[coord] = self.map.get(coord, 0) + 2
                else:
                    print(instr)
                    print("instr not found")


with open(dpath) as f:
    instructions = []
    for line in f:
        parts = line.strip().split()
        if parts[0] == "turn":
            instr = " ".join(parts[:2])
            start, end = parts[2], parts[4]
        else:
            instr = "toggle"
            start, end = parts[1], parts[3]
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        instructions.append([instr, start, end])

yard = Yard(instructions)
lights_on = list(yard.map.values()).count(1)
print(f"Part 1: {lights_on}")

yard = YardV2(instructions)
brightness = sum(yard.map.values())
print(f"Part 2: {brightness}")
