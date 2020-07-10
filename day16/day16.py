"""day16.py
"""
import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

TICKER = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
""".strip().splitlines()
TICKERDICT = {x.split(':')[0].strip(): int(x.split(':')[1].strip()) for x in TICKER}


class Aunt:
    def __init__(self, data):
        self.data = data

    def process(self):
        for line in self.data:
            r = re.match(r"Sue (\d+): (.*)", line)
            num, things = r.groups()
            things = [x.strip() for x in things.split(",")]
            if self.has_all(things):
                print(num)

            if self.has_all_2(things):
                print(num)

    def has_all(self, things):
        for thing in things:
            if thing not in TICKER:
                return False
        return True

    def has_all_2(self, things):
        for thing in things:
            key, val = thing.split(':')
            key = key.strip()
            val = int(val.strip())
            if key in ['cats', 'trees']:
                if TICKERDICT[key] >= val:
                    return False
            elif key in ['pomeranians', 'goldfish']:
                if TICKERDICT[key] <= val:
                    return False
            else:
                if TICKERDICT[key] != val:
                    return False
        return True


with open(dpath) as f:
    data = [x.strip() for x in f.readlines()]

aunt = Aunt(data)
aunt.process()
