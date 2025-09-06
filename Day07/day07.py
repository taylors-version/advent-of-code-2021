growth = dict()

def puzzle1(data):
    crabs = [int(crab) for crab in data.split(',')]
    return min([sum([abs(position - crab) for crab in crabs]) for position in range(max(crabs) + 1)])

def puzzle2(data):
    crabs = [int(crab) for crab in data.split(',')]
    return int(min([sum([(abs(position - crab)*(abs(position - crab) + 1))/2 for crab in crabs]) for position in range(max(crabs) + 1)]))


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))