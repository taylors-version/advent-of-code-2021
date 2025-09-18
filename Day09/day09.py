from functools import reduce

def puzzle1(data):
    numbers = [[int(x) for x in list(y)] for y in data]

    ben = [2,3]
    bob = numbers[ben[1]][ben[0]]

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
    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))