from functools import reduce


def puzzle1(data):
    numbers = [[int(x) for x in y] for y in data]
    ben = [neighbours([x,y]) for y in range(len(numbers)) for x in range(len(numbers[0]))]
    #alice = [[x for x in y] for y in data if reduce(lambda a,b: a and b )]
    bob = [x for x in neighbours([1,1])]
    #alice = [[x for x in numbers[i[1]][i[0]]] for i in neighbours([1,1])]

    return 0

def puzzle2(data):
    return 0

def neighbours(point):
    return [[point[0]+x,point[1]+y] for x in (-1,1) for y in (-1, 1)]

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))