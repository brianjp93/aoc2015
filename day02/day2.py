"""day2.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")


class Box:
    def __init__(self, l, w, h):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)

    def __repr__(self):
        return f"Box({self.l}, {self.w}, {self.h})"

    def surface_area_with_extra(self):
        sides = self.side_areas()
        return int(sum(sides) + (min(sides) / 2))

    def side_areas(self):
        return ((2 * self.l * self.w), (2 * self.w * self.h), (2 * self.h * self.l))

    def volume(self):
        return self.l * self.w * self.h

    def perimeters(self):
        return (
            2 * self.l + 2 * self.w,
            2 * self.w + 2 * self.h,
            2 * self.h + 2 * self.l,
        )

    def bow_length_needed(self):
        return self.volume() + min(self.perimeters())


with open(dpath) as f:
    data = [Box(*line.strip().split("x")) for line in f.readlines()]
    areas = [box.surface_area_with_extra() for box in data]
    total_area = sum(areas)
    print(total_area)

    bows = [box.bow_length_needed() for box in data]
    print(sum(bows))
