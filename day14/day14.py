"""day14.py
"""
import re


data = """
Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
""".strip().splitlines()

test = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip().splitlines()


class Race:
    def __init__(self, data):
        self.data = self.process(data)

    def process(self, data):
        out = {}
        for line in data:
            r = re.match(r"(\w+).*fly (\d+).*for (\d+).*for (\d+) seconds.", line)
            groups = r.groups()
            out[groups[0]] = [int(x) for x in groups[1:]]
        return out

    def find_distance(self, name, t):
        data = self.data[name]
        speed = data[0] * data[1]
        full_time = data[1] + data[2]
        full_rounds, leftover = divmod(t, full_time)
        distance = speed * full_rounds
        if leftover >= data[1]:
            distance += speed
        else:
            distance += leftover / data[1] * data[0]
        return distance

    def find_winner(self, t):
        max_name = []
        max_dist = -float("inf")
        for name in self.data:
            dist = self.find_distance(name, t)
            if dist > max_dist:
                max_name = [name]
                max_dist = dist
            elif dist == max_dist:
                max_name.append(name)
        return max_name, max_dist

    def award_points(self, t):
        points = {name: 0 for name in self.data}
        for i in range(1, t + 1):
            print(i)
            max_names, _ = self.find_winner(i)
            print(max_names)
            for name in max_names:
                points[name] += 1
        return points


r = Race(test)
winner, dist = r.find_winner(2503)
print(winner)
print(dist)

points = r.award_points(1000)
print(points)
