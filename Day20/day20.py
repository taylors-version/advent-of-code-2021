from collections import defaultdict

image_size = 0

def enhance(points, iea, point):
    y,x = point
    bin = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0 ,1]:
            if points[f'{y+dy},{x+dx}'] == '#':
                bin.append('1')
            else:
                bin.append('0')
    return iea[int(''.join(bin), 2)]

def process(points, iea, default):
    new_points = defaultdict(lambda: default)
    old_points = points.copy()
    for p in old_points:
        y,x = [int(n) for n in p.split(',')]
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                new_points[f'{y+dy},{x+dx}'] = enhance(points, iea, (y+dy, x+dx))

    return new_points

def init_points(image):
    points = defaultdict(lambda: '.')
    for y, _ in enumerate(image):
        for x, _ in enumerate(image[y]):
            points[f'{y},{x}'] = image[y][x]
    return points

def puzzle1(data):
    iea = data[0]
    image = data[2:]
    global image_size
    image_size = len(image)

    points = init_points(image)

    for i in range(2):
        if i % 2 == 0 or iea[0] == '.':
            default = iea[0]
        else:
            default = iea[-1]
        points = process(points, iea, default)

    return sum([1 for p in points if points[p] == '#'])

def puzzle2(data):
    iea = data[0]
    image = data[2:]
    global image_size
    image_size = len(image)

    points = init_points(image)

    for i in range(50):
        if i % 2 == 0 or iea[0] == '.':
            default = iea[0]
        else:
            default = iea[-1]
        points = process(points, iea, default)

    return sum([1 for p in points if points[p] == '#'])


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))