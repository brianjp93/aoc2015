"""day5.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

VOWELS = {x for x in "aeiou"}
REQUIRED = ["ab", "cd", "pq", "xy"]


def is_nice(line):
    if sum(c in VOWELS for c in line) < 3:
        return False
    if not any(a == b for a, b in zip(line, line[1:])):
        return False
    if any(x in line for x in REQUIRED):
        return False
    return True


def has_double_pair(line):
    for i in range(0, len(line) - 1):
        sub = line[i : i + 2]
        if line[i + 2 :].count(sub) >= 1:
            return True
    return False


def has_sandwich(line):
    for i in range(0, len(line) - 2):
        if line[i] == line[i + 2]:
            return True
    return False


def is_nice2(line):
    if all((has_double_pair(line), has_sandwich(line))):
        return True
    return False


with open(dpath) as f:
    data = [x.strip() for x in f.readlines()]
    out = sum(is_nice(x) for x in data)
    print(out)
    out = sum(is_nice2(x) for x in data)
    print(out)
