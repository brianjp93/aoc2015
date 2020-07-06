"""day12.py
"""
import pathlib
import json

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")


class JSA:
    def __init__(self, data):
        self.data = data

    def process(self, part2=False):
        return self.get_list_value(self.data, part2=part2)

    def get_list_value(self, ls, part2=False):
        out = []
        for elt in ls:
            if isinstance(elt, int):
                out.append(elt)
            elif isinstance(elt, list):
                out.append(self.get_list_value(elt, part2=part2))
            elif isinstance(elt, dict):
                out.append(self.get_dict_value(elt, part2=part2))
        return sum(out)

    def get_dict_value(self, dc, part2=False):
        out = []
        for ch, val in dc.items():
            if isinstance(val, int):
                out.append(val)
            elif isinstance(val, list):
                out.append(self.get_list_value(val, part2=part2))
            elif isinstance(val, dict):
                out.append(self.get_dict_value(val, part2=part2))
            elif part2 and val == "red":
                return 0
        return sum(out)


with open(dpath) as f:
    data = json.loads(f.read())

jsa = JSA(data)
out = jsa.process()
print(f"part 1: {out}")

out = jsa.process(part2=True)
print(f"part 2: {out}")
