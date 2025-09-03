def puzzle1(data):
    lines = data.splitlines()
    numbers = [int(line) for line in lines]
    pairs = zip(numbers, numbers[1:])
    return sum([1 for a,b in pairs if b-a > 0])

def puzzle2(data):
    lines = data.splitlines()
    numbers = [int(line) for line in lines]
    windows = [sum(n) for n in zip(numbers, numbers[1:], numbers[2:])]
    pairs = zip(windows, windows[1:])
    return sum([1 for a,b in pairs if b-a > 0])


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        print(puzzle1(data))
        print(puzzle2(data))