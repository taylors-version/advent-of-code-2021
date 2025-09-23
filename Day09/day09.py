import queue
from functools import reduce
from operator import mul


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
    numbers = [[int(x) for x in list(y)] for y in data]

    result = 0
    for y in range(len(numbers)):
        for x in range(len(numbers[y])):
            up, down, left, right = True, True, True, True
            if y > 0:
                up = numbers[y][x] < numbers[y-1][x]
            if y + 1 < len(numbers):
                down = numbers[y][x] < numbers[y+1][x]
            if x > 0:
                left = numbers[y][x] < numbers[y][x-1]
            if x + 1 < len(numbers[y]):
                right = numbers[y][x] < numbers[y][x+1]
            if up and down and left and right:
                result += numbers[y][x]+1

    return result

def puzzle2(data):
    numbers = [[int(x) for x in list(y)] for y in data]

    lows = []
    for y in range(len(numbers)):
        for x in range(len(numbers[y])):
            up, down, left, right = True, True, True, True
            if y > 0:
                up = numbers[y][x] < numbers[y-1][x]
            if y + 1 < len(numbers):
                down = numbers[y][x] < numbers[y+1][x]
            if x > 0:
                left = numbers[y][x] < numbers[y][x-1]
            if x + 1 < len(numbers[y]):
                right = numbers[y][x] < numbers[y][x+1]
            if up and down and left and right:
                lows.append(Point(x, y))

    basin_sizes = []
    for p in lows:
        points_seen = {p}
        points_queue = queue.Queue()
        points_queue.put(p)
        while not points_queue.empty():
            point = points_queue.get()
            for neighbour in get_neighbours(point, len(numbers[0]) - 1, len(numbers) - 1):
                if neighbour not in points_seen and numbers[neighbour.y][neighbour.x] != 9:
                    points_queue.put(neighbour)
                    points_seen.add(neighbour)

        basin_sizes.append(len(points_seen))
    return reduce(mul, sorted(basin_sizes)[-3:])

def get_neighbours(p, max_x, max_y):
    result = []
    if p.x > 0:
        result.append(Point(p.x-1, p.y))
    if p.y > 0:
        result.append(Point(p.x, p.y-1))
    if p.x < max_x:
        result.append(Point(p.x+1, p.y))
    if p.y < max_y:
        result.append(Point(p.x, p.y+1))
    return result

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))