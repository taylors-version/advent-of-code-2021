from queue import Queue


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
    grid=[[int(p) for p in line]for line in data]
    result = 0

    for _ in range(100):
        grid=[[p+1 for p in line] for line in grid]
        to_flash = set([Point(x,y) for (y,line) in enumerate(grid) for (x,val) in enumerate(line) if val > 9 ])
        flashed = set()
        while len(to_flash) != 0:
            p = to_flash.pop()
            flashed.add(p)
            for n in neighbours(p):
                grid[n.y][n.x] += 1
                if not n in flashed and grid[n.y][n.x] > 9:
                    to_flash.add(n)
        result += len(flashed)
        for p in flashed:
            grid[p.y][p.x] = 0

    return result

def puzzle2(data):
    grid=[[int(p) for p in line]for line in data]
    result = 0

    while True:
        grid=[[p+1 for p in line] for line in grid]
        to_flash = set([Point(x,y) for (y,line) in enumerate(grid) for (x,val) in enumerate(line) if val > 9 ])
        flashed = set()
        while len(to_flash) != 0:
            p = to_flash.pop()
            flashed.add(p)
            for n in neighbours(p):
                grid[n.y][n.x] += 1
                if not n in flashed and grid[n.y][n.x] > 9:
                    to_flash.add(n)
        for p in flashed:
            grid[p.y][p.x] = 0
        result += 1
        if len(flashed) == 100:
            break

    return result

def neighbours(point):
    points = [Point(x,y) for x in range(point.x-1,point.x+2) for y in range(point.y-1,point.y+2)]
    return set([p for p in points if (p!=point and p.x>=0 and p.y>=0 and p.x<10 and p.y<10)])
if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))