def modulo_at_1(val, mod):
    modulo = val % mod
    return mod if val == 0 else modulo

def turn(pos, next_die_val):
    add = next_die_val + modulo_at_1(next_die_val+1,100) + modulo_at_1(next_die_val + 2, 100)
    new_pos = (pos + add)%10
    return modulo_at_1(new_pos, 10)

def puzzle1(data):
    p1_pos = int(data[0].split(": ")[-1])
    p2_pos = int(data[1].split(": ")[-1])
    p1_score,p2_score,die_count = 0,0,0
    next_die = 1

    while max(p1_score, p2_score) < 1000:
        die_count = die_count+3
        if die_count % 2 == 1:
            p1_pos = turn(p1_pos, next_die)
            p1_score = p1_score + p1_pos
        else:
            p2_pos = turn(p2_pos, next_die)
            p2_score = p2_score + p2_pos
        next_die = modulo_at_1(next_die+3,100)

    ben = "hello"
    return min(p1_score, p2_score)*die_count

def puzzle2(data):
    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))