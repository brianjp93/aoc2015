"""day13.py
"""
import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")
tpath = pathlib.PurePath(CWD, "test")


class Table:
    def __init__(self, data):
        self.happiness = {}
        self.happiness_with_me = {'me': {}}
        self.process(data)

    def process(self, data):
        for line in data:
            r = re.split('would gain | would lose | happiness units by sitting next to', line)
            key = r[0].strip()
            key2 = r[2].strip().strip('.')
            ndict = self.happiness.get(key, {})
            ndict[key2] = int(r[1]) if 'gain' in line else -int(r[1])
            self.happiness[key] = ndict
        for key, val in self.happiness.items():
            self.happiness_with_me[key] = dict(val)
            self.happiness_with_me[key]['me'] = 0
            self.happiness_with_me['me'][key] = 0

    def optimize_table(self, hp=None):
        if hp is None:
            hp = self.happiness
        max_score = -float('inf')
        arrangement = []
        people = list(hp.keys())
        npeople = len(people)
        people_set = set(people)
        stack = [[[people[0]], 0]]
        while stack:
            seating, score = stack.pop()
            if len(seating) == npeople:
                score = score + hp[seating[-1]][seating[0]] + hp[seating[0]][seating[-1]]
                if score > max_score:
                    max_score = score
                    arrangement = seating
            for person in people_set - set(seating):
                nseating = seating[:] + [person]
                nscore = score + hp[seating[-1]][person] + hp[person][seating[-1]]
                stack.append([nseating, nscore])
        return arrangement, max_score


with open(dpath) as f:
    data = [x.strip() for x in f]

t = Table(data)
seating, max_score = t.optimize_table()
print(seating)
print(max_score)

seating, max_score = t.optimize_table(hp=t.happiness_with_me)
print(seating)
print(max_score)
