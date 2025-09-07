import re

display =  {
    "abcefg": '0',
    "cf": '1',
    "acdeg": '2',
    "acdfg": '3',
    "bcdf": '4',
    "abdfg": '5',
    "abdefg": '6',
    "acf": '7',
    "abcdefg": '8',
    "abcdfg": '9'
}
def puzzle1(data):
    outputted_uniques = [[a for i,a in enumerate(line) if i > 9 and len(a) in [2,3,4,7]] for line in [re.split(' \\| | ', line) for line in data]]
    return sum(len(line) for line in outputted_uniques)

def puzzle2(data):
    joined = [[a.split() for a in b.split('|')] for b in data]

    values = [int(''.join([display[''.join(sorted([dictionary[key] for key in segment]))]
                            for segment in [seen for seen in value]]))
                            for [value,dictionary] in [[b, get_dict(a)] for a,b in joined]]

    return sum(values)

def get_dict(screen):
    one = next(a for a in screen if len(a) == 2) #be
    three = next(a for a in screen if len(a) == 5 and len(set(a) & set(one)) == 2)
    six = next(a for a in screen if len(a) == 6 and len(set(a) & set(one)) == 1)
    four = next(a for a in screen if len(a) == 4)
    seven = next(a for a in screen if len(a) == 3)
    eight = next(a for a in screen if len(a) == 7)
    a = next(a for a in seven if a not in one)
    c = next(c for c in one if c not in six)
    f = next(f for f in one if f != c)
    b = next(b for b in four if b not in three)
    d = next(d for d in four if d not in [b, c, f])
    g = next(g for g in three if g not in [a,c,d,f])
    e = next(e for e in eight if e not in [a,b,c,d,f,g])
    return {a:'a',b:'b',c:'c',d:'d',e:'e',f:'f',g:'g'}


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))