from functools import reduce


def puzzle1(data):
    numbers = [int(i) for i in data[0].split(',')]

    int_parse = [[int(n) for n in card.split()] for i, card in enumerate(data[2:]) if (i+1) % 6 != 0]
    cards = [int_parse[i:i+5] for i in range(0, len(int_parse), 5)]

    return 0

def puzzle2(data):
    return 0


def check_card(numbers, card):
    checked = [[True if n in numbers else False for n in row] for row in card]
    rows = reduce(lambda x,y:x or y, [reduce(lambda x,y:x and y, row) for row in checked])
    colums = reduce(lambda x,y:x or y, [reduce(lambda x,y:x and y, column) for column in zip(*checked[::1])])
    return rows or colums

def card_score(numbers, card):
    match = [[i for i in ]]

    return 15

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))