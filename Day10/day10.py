from functools import reduce

matches = {"(":")", "[":"]", "{":"}", "<":">"}
illegal_scores = {")":3, "]":57, "}":1197, ">":25137}
completion_scores = {")":1, "]":2, "}":3, ">":4}
def puzzle1(data):

    return sum([line_check(line) for line in data])

def puzzle2(data):
    scores = sorted(list(filter(lambda x: x!=0,[reduce(lambda x, y: x*5 + y, line, 0) for line in [[completion_scores[c] for c in missing_chars(line)] for line in data]])))
    return scores[len(scores)//2]

def line_check(line):
    l = []
    for c in line:
        if c in matches:
            l.append(c)
        else:
            m = l.pop()
            if c != matches[m]:
                return illegal_scores[c]
    return 0

def missing_chars(line):
    if len(line) == 0:
        return ""
    l = []
    for c in line:
        if c in matches:
            l.insert(0,matches[c])
        elif c == l[0]:
            l.pop(0)
        else:
            return ""
    return ''.join(l)


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))