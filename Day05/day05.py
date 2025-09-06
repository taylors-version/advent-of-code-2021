import re

def puzzle1(data):
    int_parse = [[int(x) for x in re.split(',| -> ', row) if x.isdigit()] for row in data]
    hori_and_vert = [row for row in int_parse if row[0]==row[2] or row[1] == row[3]]

    points = set()
    dups = set()
    for line in hori_and_vert:
        if line[0] == line[2]:
            dots = [(line[0], y) for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1)]
        else:
            dots = [(x, line[1]) for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1)]
        dups.update(list(set(dots) & points))
        points.update(dots)

    return len(dups)

def puzzle2(data):
    lines = [[int(x) for x in re.split(',| -> ', row) if x.isdigit()] for row in data]

    points = set()
    dups = set()
    for line in lines:
        if line[0] == line[2]:
            dots = [(line[0], y) for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1)]
        elif line[1] == line[3]:
            dots = [(x, line[1]) for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1)]
        else:
            if (line[0] - line[2]) * (line[1] - line[3]) > 0:
                dots = [(min(line[0], line[2])+i, min(line[1], line[3])+i) for i in range(abs(line[0]-line[2])+1)]
            else:
                dots = [(min(line[0], line[2])+i, max(line[1], line[3])-i) for i in range(abs(line[0]-line[2])+1)]
        dups.update(list(set(dots) & points))
        points.update(dots)

    return len(dups)

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))