"""day4.py
"""
from itertools import count
from hashlib import md5

KEY = "iwrupvqb"


def get_key(zeroes=5):
    for i in count():
        data = f"{KEY}{i}"
        out = md5(data.encode())
        out = out.hexdigest()
        if out.startswith("0" * zeroes):
            return i


print(get_key(5))
print(get_key(6))
