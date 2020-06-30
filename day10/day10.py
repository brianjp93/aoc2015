"""day10.py
"""

data = "1113122113"


def look_and_say(seq):
    out = [[seq[0], 1]]
    for n in seq[1:]:
        if n == out[-1][0]:
            out[-1][1] += 1
        else:
            out.append([n, 1])
    nout = []
    for elt in out:
        nout += [str(elt[1]), elt[0]]
    return "".join(nout)


def look_and_say_iterate(seq, n=1):
    for i in range(n):
        seq = look_and_say(seq)
    return seq


seq = look_and_say_iterate(data, 40)
print(len(seq))

seq = look_and_say_iterate(data, 50)
print(len(seq))
