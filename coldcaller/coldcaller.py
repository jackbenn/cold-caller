import sys
import random

class ColdCaller:
    
    def __init__(self, names=None):
        self.students = {name: 1.0 for name in names}
        self._normalize()
        self.ratio = 0.5
        self.sequence = []

    def _normalize(self):
        total = sum(self.students.values())
        for name in self.students:
            self.students[name] /= total

    def choose(self):
        winner = random.choices(list(self.students.keys()),
                                list(self.students.values()),
                                k=1)[0]
        self.students[winner] *= self.ratio
        self._normalize()
        return winner

    def hist(self):
        hist = '\n'
        for name, prob in self.students.items():
            hist += f'{name:10s}' + '*' * int(prob * 50) + '\n'
        return hist

   def undo(self):
        name = sequence.pop()
        self.students[name] /= self.ratio
        self._normalize()



if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        names = [name.strip() for name in f.readlines()]
    cc = ColdCaller(names)
    for _ in range(20):
        print(cc.hist())
        print(cc.choose())

