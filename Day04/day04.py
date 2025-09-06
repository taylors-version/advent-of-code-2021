from functools import reduce


def puzzle1(data):
    numbers = [int(i) for i in data[0].split(',')]

    int_parse = [[int(n) for n in card.split()] for i, card in enumerate(data[2:]) if (i+1) % 6 != 0]
    cards = [int_parse[i:i+5] for i in range(0, len(int_parse), 5)]
    for i in range(len(numbers)):
        for card in cards:
            if check_card(numbers[:i + 1], card):
                return card_score(numbers[:i+1], card) * numbers[i]

    return 0

def puzzle2(data):
    numbers = [int(i) for i in data[0].split(',')]

    int_parse = [[int(n) for n in card.split()] for i, card in enumerate(data[2:]) if (i+1) % 6 != 0]
    cards = [int_parse[i:i+5] for i in range(0, len(int_parse), 5)]

    for i in range(len(numbers)):
        for card in cards:
            if check_card(numbers[:i + 1], card):
                if len(cards) > 1:
                    cards.remove(card)
                else:
                    return card_score(numbers[:i+1], card) * numbers[i]
    return 0


def check_card(numbers, card):
    checked = [[True if n in numbers else False for n in row] for row in card]
    rows = reduce(lambda x,y:x or y, [reduce(lambda x,y:x and y, row) for row in checked])
    columns = reduce(lambda x,y:x or y, [reduce(lambda x,y:x and y, column) for column in zip(*checked[::1])])
    return rows or columns

def card_score(numbers, card):
    match = [[num for num in row if num not in numbers] for row in card]
    return reduce(lambda x, y: x + sum(y), match, 0)

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))