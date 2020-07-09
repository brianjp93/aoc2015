"""day15.py
"""

data = """
Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
""".strip().splitlines()


class Cookie:
    def __init__(self, data):
        self.data = self.process(data)

    def process(self, data):
        out = {}
        for line in data:
            item, features = line.split(':')
            features = features.strip().split(',')
            out[item] = {x.split()[0]: int(x.split()[1]) for x in features}
        return out

c = Cookie(data)
print(c.data)
