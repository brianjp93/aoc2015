"""day9.py
"""
import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")


class NodeMap:
    def __init__(self):
        self.locations = {}

    def add_node(self, location):
        if location not in self.locations:
            self.locations[location] = Node(location)

    def get_shortest_path(self):
        shortest_dist = float("inf")
        shortest_path = None
        path_len = len(self.locations)
        stack = [([x.loc], 0) for x in self.locations.values()]
        while stack:
            path, dist = stack.pop()
            path_set = set(path)
            node = path[-1]
            if len(path) == path_len:
                if dist < shortest_dist:
                    shortest_dist = dist
                    shortest_path = path
            else:
                for next_node, next_dist in self.locations[node].destination.items():
                    if next_node.loc not in path_set:
                        stack.append((path[:] + [next_node.loc], dist + next_dist))
        return shortest_path, shortest_dist

    def get_longest_path(self):
        longest_dist = 0
        longest_path = None
        path_len = len(self.locations)
        stack = [([x.loc], 0) for x in self.locations.values()]
        while stack:
            path, dist = stack.pop()
            path_set = set(path)
            node = path[-1]
            if len(path) == path_len:
                if dist > longest_dist:
                    longest_dist = dist
                    longest_path = path
            else:
                for next_node, next_dist in self.locations[node].destination.items():
                    if next_node.loc not in path_set:
                        stack.append((path[:] + [next_node.loc], dist + next_dist))
        return longest_path, longest_dist


class Node:
    def __init__(self, loc):
        self.loc = loc
        self.destination = {}

    def __repr__(self):
        return f"Node(loc={self.loc}, destination={len(self.destination)})"

    def add_destination(self, destination, distance):
        self.destination[destination] = distance


nm = NodeMap()
with open(dpath) as f:
    for line in f:
        line = line.strip()
        p1, p2 = line.split("=")
        p2 = p2.strip()
        loc1, loc2 = tuple(x.strip() for x in p1.split("to"))
        nm.add_node(loc1)
        nm.add_node(loc2)
        nm.locations[loc1].add_destination(nm.locations[loc2], int(p2))
        nm.locations[loc2].add_destination(nm.locations[loc1], int(p2))

path, dist = nm.get_shortest_path()
print(path, dist)

path, dist = nm.get_longest_path()
print(path, dist)
