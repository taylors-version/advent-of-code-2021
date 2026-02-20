import itertools
import math
from functools import reduce

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
            path = added.traverse_to_depth4()
            if path is not None:
                exploding = added.val_from_path(path)
                added.explode_left(path, exploding.a)
                added.explode_right(path, exploding.b)
                parent = added.val_from_path(path[:-1])
                if path[-1] == "L":
                    parent.a = 0
                else:
                    parent.b = 0
            else:
                path = added.find_val_greater_9()
                if path is not None:
                    splitting = added.val_from_path(path)
                    l = splitting // 2
                    r = int(math.ceil(splitting/2))
                    parent = added.val_from_path(path[:-1])
                    new_sf = SnailFish(l,r)
                    if path[-1] == "L":
                        parent.a = new_sf
                    else:
                        parent.b = new_sf
                else:
                    needs_reducing = False
        return added

    def traverse_to_depth4(self, path=None):
        if path is None:
            path = []
        if len(path) == 4:
            return path
        if isinstance(self.a, SnailFish):
            poss = self.a.traverse_to_depth4(path + ["L"])
            if poss is not None:
                return poss
        if isinstance(self.b, SnailFish):
            poss = self.b.traverse_to_depth4(path + ["R"])
            if poss is not None:
                return poss
        return None

    def explode_left(self, path, val):
        left_path = path.copy()
        left_path.reverse()
        first_r = next((n for n,p in enumerate(left_path) if p =='R'), None)
        if first_r is None:
            return
        left_path = left_path[first_r+1:]
        left_path.reverse()
        left_path.append("L")
        left = self
        while isinstance(left, SnailFish):
            left = self.val_from_path(left_path)
            left_path.append("R")
        left_path = left_path[:-1]
        if left_path[-1] == "R":
            self.val_from_path(left_path[:-1]).b = left + val
        else:
            self.val_from_path(left_path[:-1]).a = left + val

    def explode_right(self, path, val):
        right_path = path.copy()
        right_path.reverse()
        first_l = next((n for n,p in enumerate(right_path) if p =='L'), None)
        if first_l is None:
            return
        right_path = right_path[first_l+1:]
        right_path.reverse()
        right_path.append("R")
        right = self
        while isinstance(right, SnailFish):
            right = self.val_from_path(right_path)
            right_path.append("L")
        right_path = right_path[:-1]
        if right_path[-1] == "L":
            self.val_from_path(right_path[:-1]).a = right + val
        else:
            self.val_from_path(right_path[:-1]).b = right + val

    def find_val_greater_9(self, path=None):
        if path is None:
            path = []
        if isinstance(self.a, SnailFish):
                poss = self.a.find_val_greater_9(path + ["L"])
                if poss is not None:
                    return poss
        if isinstance(self.a, int) and self.a > 9:
            return path + ["L"]
        if isinstance(self.b, SnailFish):
            poss = self.b.find_val_greater_9(path + ["R"])
            if poss is not None:
                return poss
        if isinstance(self.b, int) and self.b > 9:
            return path + ["R"]
        return None

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

    def val_from_path(self, path):
        if path is None or len(path) == 0:
            return self
        elif path[0] == "L":
            if isinstance(self.a, int):
                return self.a if len(path) == 1 else None
            return self.a.val_from_path(path[1:])
        else:
            if isinstance(self.b, int):
                return self.b if len(path) == 1 else None
            return self.b.val_from_path(path[1:])

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
    sfs = [SnailFish.from_string(s) for s in data]
    sf = reduce(lambda a, b: a.add(b), sfs)
    return sf.magnitude()


def puzzle2(data):
    return 0


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))