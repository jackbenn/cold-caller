import sys
import random


class ColdCaller:

    def __init__(self, names=None):
        self.students = None
        self.ratio = 0.5
        self.sequence = None

    def read_names(self, filename):
        with open(filename) as f:
            names = [name.strip() for name in f.readlines()]

        self.students = {name: 1.0 for name in names}
        self._normalize()
        self.sequence = []

    def read_state(self, filename):
        with open(filename) as f:
            self.sequence = f.readline().strip().split(',')
            self.students = {}
            for line in f:
                name, probability = line.split(',')
                self.students[name] = float(probability.strip())
            self._normalize()
    
    def write_state(self, filename):
        with open(filename, 'w') as f:
            f.write(','.join(self.sequence))
            f.write('\n')
            for name in self.students:
                f.write(f"{name},{self.students[name]}\n")

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
        self.sequence.append(winner)
        return winner

    def hist(self):
        hist = '\n'
        for name, prob in self.students.items():
            hist += f'{name:10s}' + '*' * int(prob * 50) + '\n'
        return hist

    def undo(self):
        name = self.sequence.pop()
        self.students[name] /= self.ratio
        self._normalize()


if __name__ == '__main__':
    filename = sys.argv[1]
    cc = ColdCaller()
    cc.read_names(filename)
    for _ in range(20):
        print(cc.hist())
        print(cc.choose())
    print(cc.hist())
    cc.undo()
    print("undoing")
    print(cc.hist())
    print(cc.choose())
    cc.write_state("temp.txt")
