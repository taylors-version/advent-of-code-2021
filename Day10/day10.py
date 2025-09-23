matches = {"(":")", "[":"]", "{":"}", "<":">"}
scores = {")":3, "]":57, "}":1197, ">":25137}
def puzzle1(data):

    return sum([line_check(line) for line in data])

def puzzle2(data):
    return 0

def line_check(line):
    l = []
    for c in line:
        if c in matches:
            l.append(c)
        else:
            m = l.pop()
            if c != matches[m]:
                return scores[c]
    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))