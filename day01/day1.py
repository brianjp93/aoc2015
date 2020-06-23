"""day01.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

with open(dpath, "r") as f:
    data = f.read().strip()
    out = data.count("(") - data.count(")")

print(f"Floor: {out}")


floor = 0
seen = {}
with open(dpath, "r") as f:
    data = f.read().strip()
    for i, c in enumerate(data, 1):
        floor = floor + 1 if c == "(" else floor - 1
        if floor not in seen:
            seen[floor] = i

print(f"Position: {seen[-1]}")
