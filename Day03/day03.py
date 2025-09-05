
def puzzle1(data):

    total = pow(2, len(data.splitlines()[0])) - 1
    most_common = list(max(set(line), key=line.count) for line in list(zip(*data.splitlines()[::1])))
    gamma = int(''.join(map(str, most_common)), 2)

    return gamma * (total - gamma)

def puzzle2(data):
    lines = data.splitlines()
    oxygen = lines
    co2 = lines
    for i in range(len(lines[0])):
        if len(oxygen) > 1:
            oxygen_ones  = [l for l in oxygen if l[i] == "1"]

            if len(oxygen_ones) >= len(oxygen)/2:
                oxygen = oxygen_ones
            else:
                oxygen = [l for l in oxygen if l not in oxygen_ones]

        if len(co2) > 1:
            co2_zeroes = [l for l in co2 if l[i] == "0"]
            if len(co2_zeroes) <= len(co2)/2:
                co2 = co2_zeroes
            else:
                co2 = [l for l in co2 if l not in co2_zeroes]

    oxygen = int(''.join(map(str, oxygen[0])), 2)
    co2 = int(''.join(map(str, co2[0])), 2)
    return oxygen * co2


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        print(puzzle1(data))
        print(puzzle2(data))