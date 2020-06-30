"""day11.py
"""
from string import ascii_lowercase

data = "hxbxwxba"
LETTER_RANGE = list(range(26))
INVALID = {ascii_lowercase.index(x) for x in "iol"}


def increment_password(seq):
    seq.reverse()
    for i in range(len(seq)):
        seq[i] = (seq[i] + 1) % 26
        if seq[i] in INVALID:
            seq[i] += 1
        if seq[i] != 0:
            break
    seq.reverse()
    return seq


def init_seq(seq):
    for i in range(len(seq)):
        if seq[i] in INVALID:
            seq[i] += 1
            break
    for i in range(i + 1, len(seq)):
        seq[i] = 0
    return seq


def is_password_valid(seq):
    return all((has_straight(seq), not has_invalid_letters(seq), has_2_pairs(seq)))


def has_straight(seq):
    for a, b, c in zip(seq, seq[1:], seq[2:]):
        if a == b - 1 and b == c - 1:
            return True
    return False


def has_invalid_letters(seq):
    for n in seq:
        if n in INVALID:
            return True
    return False


def has_2_pairs(seq):
    count = 0
    i = 0
    while i < len(seq) - 1:
        if seq[i] == seq[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    if count >= 2:
        return True
    return False


def convert_num_to_string(seq):
    return "".join(ascii_lowercase[i] for i in seq)


def convert_string_to_num(s):
    return [ascii_lowercase.index(ch) for ch in s]


def find_next_password(password):
    seq = convert_string_to_num(password)
    seq = increment_password(seq)
    seq = init_seq(seq)
    while not is_password_valid(seq):
        seq = increment_password(seq)
    new_password = convert_num_to_string(seq)
    return new_password


new_password = find_next_password(data)
print(f"part 1: {new_password}")

new_password = find_next_password(new_password)
print(f"part 2: {new_password}")
