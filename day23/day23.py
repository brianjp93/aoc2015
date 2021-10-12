import pathlib
from typing import List

CWD = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(CWD, "data")

with open(dpath) as f:
    data = f.read().replace(',', '').splitlines()


class Computer:
    def __init__(self, instructions: List[str], a=0, b=0):
        self.reg = {
            'a': a,
            'b': b,
        }
        self.instr = instructions
        self.i = 0

    def run(self):
        while 0 <= self.i < len(self.instr):
            instr = self.instr[self.i].split()
            match instr:
                case ['hlf', r]:
                    self.reg[r] //= 2
                    self.i += 1
                case ['tpl', r]:
                    self.reg[r] *= 3
                    self.i += 1
                case ['inc', r]:
                    self.reg[r] += 1
                    self.i += 1
                case ['jmp', n]:
                    n = int(n)
                    self.i += n
                case ['jie', r, n]:
                    n = int(n)
                    if self.reg[r] % 2 == 0:
                        self.i += n
                    else:
                        self.i += 1
                case ['jio', r, n]:
                    n = int(n)
                    if self.reg[r] == 1:
                        self.i += n
                    else:
                        self.i += 1
                case _:
                    raise Exception(f'Unknown command: {instr}')


computer = Computer(data)
computer.run()
print(computer.reg['b'])

computer = Computer(data, a=1)
computer.run()
print(computer.reg['b'])
