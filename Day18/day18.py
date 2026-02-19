import itertools


class SnailFish:
    def __init__(self, a, b, depth = 0):
        self.a = a
        self.b = b

    def __str__(self):
        return "[" + str(self.a) + "," + str(self.b) + "]"

    def add(self, sf):
        added = SnailFish(self, sf)
        needs_reducing = True
        while needs_reducing:
            added_str = str(added)
            lb = 0
            i = 0
            while i < len(added_str):
                if added_str[i] == '[':
                    lb += 1
                elif added_str[i] == ']':
                    lb -= 1
                if lb > 4:
                    comma = next(n for n,c in enumerate(added_str[i:]) if c == ',')
                    rb = next(n for n,c in enumerate(added_str[i:]) if c == ']')
                    #l = len(added_str[:i]) - next(n for n,c in enumerate(reversed(added_str[:i])) if is)
                    l = int(added_str[i+1:i+comma])
                    r = int(added_str[i+comma+1:i+rb])

                    ben = "hello"
                    pass
                i += 1
            needs_reducing = False
        return added

    def magnitude(self):
        return 3*self.mag_l() + 2*self.mag_r()

    def mag_l(self):
        if isinstance(self.a, int):
            return self.a
        else:
            return self.a.magnitude()

    def mag_r(self):
        if isinstance(self.b, int):
            return self.b
        else:
            return self.b.magnitude()

    @staticmethod
    def from_string(text, depth = 0):
        text = text[1:-1]
        if text[0].isdigit():
            a = int(''.join(itertools.takewhile(lambda x: x.isdigit(), text)))
        else:
            lb = 1
            i = 0
            while lb > 0:
                i += 1
                if text[i] == '[':
                    lb += 1
                elif text[i] == ']':
                        lb -= 1
            a = SnailFish.from_string(text[0:i+1], depth+1)
        if text[-1].isdigit():
            b = int(''.join(itertools.takewhile(lambda x: x.isdigit(), reversed(text)))[::-1])
        else:
            rb = 1
            i = -1
            while rb > 0:
                i -=1
                if text[i] == ']':
                    rb += 1
                elif text[i] == '[':
                    rb -= 1
            b = SnailFish.from_string(text[i:], depth+1)
        return SnailFish(a, b, depth)


def puzzle1(data):
    return 0


def puzzle2(data):
    return 0


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))