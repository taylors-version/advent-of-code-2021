from collections import Counter, defaultdict


def puzzle1(data):
    polymer = data[0]
    rules = {a[0]:a[1] for a in [rule.split(" -> ") for rule in data[2:]]}
    for i in range(10):
        polymer = step(polymer, rules)
    counts = [c[1] for c in Counter(polymer).items()]

    return max(counts) - min(counts)

def puzzle2(data):
    pairs = defaultdict(int)
    rules = {a[0]:a[1] for a in [rule.split(" -> ") for rule in data[2:]]}
    for k,v in Counter([data[0][i:i+2] for i in range(len(data[0])-1)]).items():
        pairs[k] += v

    for i in range(40):
        new_pairs = defaultdict(int)
        for k,v in pairs.items():
            insertion = rules[k]
            new_pairs[k[0]+insertion] += v
            new_pairs[insertion+k[1]] += v
        pairs = new_pairs

    counts = defaultdict(int)
    for k,v in pairs.items():
        counts[k[0]] += v
        counts[k[1]] += v
    counts[data[0][0]] += 1
    counts[data[0][-1]] += 1
    for k,v in counts.items():
        counts[k] = v/2

    return max(counts.values()) - min(counts.values())

def step(polymer, rules):
    inserts = [rules[pair] for pair in [polymer[i:i+2] for i in range(len(polymer)-1)]]
    return ''.join([polymer[i]+ inserts[i] for i in range(len(polymer)-1)]) + polymer[-1]

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))