class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def puzzle1(data):
    dots = [Point(int(x), int(y)) for x,y in [line.split(",") for line in data if len(line) > 0 and line[0].isdigit()]]
    folds = [line.split()[2].split("=") for line in data if line.startswith("fold")]

    return len(fold(dots, folds[0]))

def puzzle2(data):
    dots = [Point(int(x), int(y)) for x,y in [line.split(",") for line in data if len(line) > 0 and line[0].isdigit()]]
    folds = [line.split()[2].split("=") for line in data if line.startswith("fold")]
    for method in folds:
        dots = fold(dots, method)
    result = ""
    for y in range(max([dot.y for dot in dots]) + 1):
        for x in range(max([dot.x for dot in dots]) + 1):
            if Point(x,y) in dots:
                result = result + "#"
            else:
                result = result + "."
        result = result + "\n"
    return result

def fold(dots, method):
    pivot = int(method[1])
    if method[0] == "x":
        return set([dot for dot in dots if dot.x < pivot] + [Point(2*pivot - dot.x, dot.y) for dot in dots if dot.x > pivot])
    else:
        return set([dot for dot in dots if dot.y < pivot] + [Point(dot.x, 2*pivot - dot.y) for dot in dots if dot.y > pivot])

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))