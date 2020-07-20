"""day17.py

* brute force method
I know there is come better way to do this with
some kind of dynamic programming solution but I
wasn't sure how to do it.

"""
from itertools import combinations

data = """
50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40
""".strip().splitlines()

CONTAINERS = [int(x) for x in data]


def find_ways(liters):
    count = 0
    for i in range(1, len(CONTAINERS) + 1):
        all_combs = combinations(CONTAINERS, i)
        for comb in all_combs:
            if sum(comb) == liters:
                count += 1
    return count


def find_ways_for_min(liters):
    buckets = float("inf")
    count = 0
    for i in range(1, len(CONTAINERS) + 1):
        all_combs = combinations(CONTAINERS, i)
        for comb in all_combs:
            if sum(comb) == liters:
                if len(comb) < buckets:
                    buckets = len(comb)
                    count = 1
                elif len(comb) == buckets:
                    count += 1
    return buckets, count


print(find_ways(150))
print(find_ways_for_min(150))
