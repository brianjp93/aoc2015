"""day8.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

with open(dpath) as f:
    data = [line.strip() for line in f]


def convert(s):
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\":
            if s[i + 1] == "x":
                out.append("-")
                i += 4
            else:
                out.append(s[i + 1])
                i += 2
        else:
            i += 1
            out.append(ch)
    return "".join(out)


def convert_new_string(s):
    out = ['"']
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in ["\\", '"']:
            out.append("\\" + ch)
        else:
            out.append(ch)
        i += 1
    out.append('"')
    return "".join(out)


total_literal = 0
total = 0
for line in data:
    total_literal += len(line)
    line = line[1:-1]

    line = convert(line)
    total += len(line)

print(f"Part 1: {total_literal - total}")

total = 0
for line in data:
    line = convert_new_string(line)
    total += len(line)

print(f"Part 2: {total - total_literal}")
