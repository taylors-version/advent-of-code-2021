import math
from heapq import heapify, heappop, heappush


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_value(self, data):
        x_length = len(data[0])
        y_length = len(data[0])
        x_multiple = int(self.x / x_length)
        y_multiple = int(self.y / y_length)
        val = int(data[self.y % y_length][self.x % x_length]) + x_multiple + y_multiple
        return val if val < 10 else val - 9
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __lt__(self, other):
        if self.x < other.x:
            return True
        if self.x == other.x and self.y < other.y:
            return True
        return False
    def __le__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return self < other

def puzzle1(data):
    end = Point(len(data[0])-1, len(data)-1)
    queue = [(0, Point(0,0))]
    heapify(queue)
    distances = {Point(x,y): math.inf for y in (range(len(data))) for x in range(len(data[0]))}
    distances[Point(0,0)] = 0
    visited = set()

    while queue:
        dist, point = heappop(queue)
        if point == end:
            return dist
        if point not in visited:
            visited.add(point)
            for p in neighbours(point, end.x, end.y):
                tent_dist = dist + int(data[p.y][p.x])
                if tent_dist < distances[p]:
                    distances[p] = tent_dist
                    heappush(queue, (tent_dist, p))


    return 0

def puzzle2(data):
    end = Point(len(data[0])*5-1, len(data)*5-1)
    queue = [(0, Point(0,0))]
    heapify(queue)
    distances = {Point(x,y): math.inf for y in (range(len(data) * 5)) for x in range(len(data[0]) * 5)}
    distances[Point(0,0)] = 0
    visited = set()

    while queue:
        dist, point = heappop(queue)
        if point == end:
            return dist
        if point not in visited:
            visited.add(point)
            for p in neighbours(point, end.x, end.y):
                tent_dist = dist + p.get_value(data)
                if tent_dist < distances[p]:
                    distances[p] = tent_dist
                    heappush(queue, (tent_dist, p))


    return 0

def neighbours(point, max_x, max_y):
    points = []
    if point.x > 0:
        points.append(Point(point.x - 1, point.y))
    if point.y > 0:
        points.append(Point(point.x, point.y - 1))
    if point.x < max_x:
        points.append(Point(point.x + 1, point.y))
    if point.y < max_y:
        points.append(Point(point.x, point.y + 1))
    return points

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))