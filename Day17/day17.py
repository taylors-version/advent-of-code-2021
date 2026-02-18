import re


def puzzle1(data):
    digits = [int(val) for val in re.findall("-?\\d+", data)]
    return (digits[2] + 1) * digits[2] //2


def puzzle2(data):
    digits = [int(val) for val in re.findall("-?\\d+", data)]
    v, n = 0, int((digits[0] * 2) ** 0.5 - 1)

    for dy_init in range(digits[2], -digits[2]):
        for dx_init in range(n, digits[1] + 1):
            x, y, dx ,dy = 0, 0, dx_init, dy_init
            while x <= digits[1] and y >= digits[2] and (dx == 0 and digits[0] <= x or dx != 0):
                x += dx
                y += dy
                if dx > 0: dx -= 1
                dy -= 1
                if digits[0] <= x <= digits[1] and digits[2] <= y <= digits[3]:
                    v+=1
                    break
    return v


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))