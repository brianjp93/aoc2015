"""day21.py
"""
from __future__ import annotations
import pathlib
import re
import itertools


CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "test")
ITEMS = '''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''.strip()
REGEX = r'(\w+(?:\s\+\d+)?)\s+(\d+)\s+(\d+)\s+(\d+)'

BOSS_STATS = [int(x.split(':')[1]) for x in '''
Hit Points: 103
Damage: 9
Armor: 2
'''.strip().splitlines()]

items = {}
with open(dpath) as f:
    data = f.read().split('\n\n')
    for ty, part in zip(['weapons', 'armor', 'rings'], data):
        matches = re.findall(REGEX, part)
        for m in matches:
            d = {
                'name': m[0],
                'cost': int(m[1]),
                'damage': int(m[2]),
                'armor': int(m[3]),
            }
            if ty not in items:
                items[ty] = []
            items[ty].append(d)


class Player:
    def __init__(self, hp: int, damage: int, armor: int):
        self.damage = damage
        self.armor = armor
        self.hp = hp

    def __str__(self):
        return f'Player(hp={self.hp}, damage={self.damage}, armor={self.armor})'

    def __or__(self, other: Player):
        '''Fight.
        '''
        while True:
            if self.my_turn(other):
                return True
            elif self.other_turn(other):
                return False

    def my_turn(self, other: Player):
        dmg = self.damage - other.armor
        dmg = max(dmg, 1)
        other.hp -= dmg
        return other.hp <= 0

    def other_turn(self, other: Player):
        dmg = other.damage - self.armor
        dmg = max(dmg, 1)
        self.hp -= dmg
        return self.hp <= 0


def get_boss():
    return Player(*BOSS_STATS)

def get_stats(stats):
    ret = {'cost': 0, 'armor': 0, 'damage': 0}
    for st in stats:
        ret['cost'] += st['cost']
        ret['armor'] += st['armor']
        ret['damage'] += st['damage']
    return ret


poss = itertools.product(*items.values())
lowest_cost = float('inf')
for p in poss:
    st = get_stats(p)
    player = Player(100, st['damage'], st['armor'])
    boss = get_boss()
    if player | boss:
        lowest_cost = min(lowest_cost, st['cost'])

vals = list(items.values())
vals = vals + [vals[-1]]
poss = itertools.product(*vals)
highest_cost = 0
for p in poss:
    names = {x['name'] for x in p}
    if len(names) < len(p):
        continue
    st = get_stats(p)
    player = Player(100, st['damage'], st['armor'])
    boss = get_boss()
    if boss | player:
        highest_cost = max(highest_cost, st['cost'])

print(lowest_cost)
print(highest_cost)
