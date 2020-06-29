"""day7.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")
tpath = pathlib.PurePath(CWD, "test")

MAXNUM = 2 ** 16


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.mapping = {}
        self.back = {}
        self.values = {}
        self.create_map()

    def create_map(self):
        for instr in self.instructions:
            p1, p2 = tuple(map(lambda x: x.strip(), instr.split("->")))
            p1_parts = p1.split()
            if len(p1_parts) == 3:
                if "SHIFT" in p1:
                    self.back[p2] = [p1[0]]
                else:
                    self.back[p2] = [p1_parts[0], p1_parts[2]]
            elif len(p1_parts) == 2:
                self.back[p2] = [p1_parts[1]]
            elif len(p1_parts) == 1:
                self.back[p2] = [p1_parts[0]]
            self.mapping[p2] = p1

    def get_value(self, wire):
        if wire in self.values:
            return self.values[wire]
        else:
            instr = self.mapping[wire]
            if len(instr.split()) == 1:
                if instr.isdigit():
                    self.values[wire] = int(instr)
                    return int(instr)
                else:
                    return self.get_value(instr)
            else:
                if "AND" in instr:
                    val = self.do_and(instr)
                elif "SHIFT" in instr:
                    val = self.do_shift(instr)
                elif "OR" in instr:
                    val = self.do_or(instr)
                elif "NOT" in instr:
                    val = self.do_not(instr)
                else:
                    print("instruction not found")
                self.values[wire] = val
                return val

    def do_and(self, instr):
        parts = instr.split("AND")
        p1 = parts[0].strip()
        if not p1.isdigit():
            p1 = self.get_value(p1)
        else:
            p1 = int(p1)
        p2 = parts[1].strip()
        if not p2.isdigit():
            p2 = self.get_value(p2)
        else:
            p2 = int(p2)
        return p1 & p2

    def do_not(self, instr):
        num = self.get_value(instr.split()[1])
        num = f"{num:0b}"
        num = ((16 - len(num)) * "0") + num
        num = "".join(["1" if x == "0" else "0" for x in num])
        out = int(num, 2)
        return out % MAXNUM

    def do_or(self, instr):
        parts = instr.split("OR")
        p1 = parts[0].strip()
        if not p1.isdigit():
            p1 = self.get_value(p1)
        else:
            p1 = int(p1)
        p2 = parts[1].strip()
        if not p2.isdigit():
            p2 = self.get_value(p2)
        else:
            p2 = int(p2)
        return p1 | p2

    def do_shift(self, instr):
        if "LSHIFT" in instr:
            parts = instr.split("LSHIFT")
            out = self.get_value(parts[0].strip()) << int(parts[1].strip())
            return out % MAXNUM
        elif "RSHIFT" in instr:
            parts = instr.split("RSHIFT")
            return self.get_value(parts[0].strip()) >> int(parts[1].strip())


with open(dpath) as f:
    data = [line.strip() for line in f]

comp = Computer(data)
out = comp.get_value("a")
print(f"part 1: {out}")

comp.mapping["b"] = str(out)
comp.values = {}
out = comp.get_value("a")
print(f"part 2: {out}")
