import locale


def puzzle1(data):
    lines = data.splitlines()
    forward = sum([int(l[-1]) for l in lines if l.startswith("forward")])
    down = sum([int(l[-1]) for l in lines if l.startswith("down")])
    up = sum([int(l[-1]) for l in lines if l.startswith("up")])

    return (down - up) * forward

def puzzle2(data):
    aim, horizontal, depth = 0, 0, 0
    steps = [l.strip().split(' ') for l in data.splitlines()]
    steps = [[change, int(value)] for change, value in steps]
    for change, value in steps:
        if change == "forward":
            horizontal += value
            depth += aim * value
        elif change =="down":
            aim += value
        else:
            aim -= value
    return horizontal * depth


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        print(puzzle1(data))
        print(puzzle2(data))