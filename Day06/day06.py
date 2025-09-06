growth = dict()

def puzzle1(data):
    return sum([calc_fash(int(fish), 80) for fish in data.split(',')])

def puzzle2(data):
    return sum([calc_fash(int(fish), 256) for fish in data.split(',')])

def calc_fash(fish_number, days):
    if (fish_number, days) in growth:
        return growth[(fish_number, days)]
    if days == 0:
        growth[(fish_number, days)] = 1
    elif fish_number > 0:
        growth[(fish_number, days)] = calc_fash(fish_number - 1, days - 1)
    else:
        growth[(fish_number, days)] = calc_fash(6, days - 1) + calc_fash(8, days - 1)
    return calc_fash(fish_number, days)


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))