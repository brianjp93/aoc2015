"""day18.py
"""
import pathlib


CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")
ON = "#"
OFF = "."
SURROUNDING = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


class Lights:
    def __init__(self, config):
        self.config = self.process(config)
        self.max_x = len(config[0])
        self.max_y = len(config)

    def process(self, config):
        out = {}
        for y, row in enumerate(config):
            for x, ch in enumerate(row):
                coord = (x, y)
                out[coord] = ch
        return out

    def next(self, corners_on=False):
        new_state = {}
        if corners_on:
            for coord in [
                (0, 0),
                (self.max_x - 1, 0),
                (0, self.max_y - 1),
                (self.max_x - 1, self.max_y - 1),
            ]:
                self.config[coord] = ON
        for y in range(self.max_y):
            for x in range(self.max_x):
                coord = (x, y)
                count = self.count_surrounding_on(coord)
                if self.config.get(coord) == ON:
                    if count in (2, 3):
                        new_state[coord] = ON
                    else:
                        new_state[coord] = OFF
                else:
                    if count == 3:
                        new_state[coord] = ON
                    else:
                        new_state[coord] = OFF
        if corners_on:
            for coord in [
                (0, 0),
                (self.max_x - 1, 0),
                (0, self.max_y - 1),
                (self.max_x - 1, self.max_y - 1),
            ]:
                new_state[coord] = ON
        self.config = new_state

    def count_surrounding_on(self, coord):
        count = 0
        for rel in SURROUNDING:
            ncoord = tuple(a + b for a, b in zip(coord, rel))
            if self.config.get(ncoord, OFF) == ON:
                count += 1
        return count

    def show(self):
        out = []
        for y in range(self.max_y):
            out.append("".join(self.config[(x, y)] for x in range(self.max_x)))
        return "\n".join(out)

    def go(self, n, corners_on=False):
        for _ in range(n):
            self.next(corners_on=corners_on)


with open(dpath, "r") as f:
    data = [line.strip() for line in f]

lights = Lights(data)
lights.go(100)
print(list(lights.config.values()).count(ON))


lights = Lights(data)
lights.go(100, corners_on=True)
print(list(lights.config.values()).count(ON))
