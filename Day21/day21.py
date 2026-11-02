class State:
    def __init__(self, p1_pos, p2_pos, p1_score, p2_score, next_player):
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.next_player = next_player

    def roll(self, dice_sum):
        if self.next_player == 1:
            new_p1_pos = modulo_at_1(self.p1_pos+dice_sum, 10)
            return State(new_p1_pos, self.p2_pos,self.p1_score+new_p1_pos, self.p2_score, 2)
        else:
            new_p2_pos = modulo_at_1(self.p2_pos+dice_sum, 10)
            return State(self.p1_pos, new_p2_pos,self.p1_score, self.p2_score+new_p2_pos, 1)

    def __eq__(self, other):
        return self.p1_pos == other.p1_pos and self.p2_pos == other.p2_pos and self.p1_score == other.p1_score and self.p2_score == other.p2_score and self.next_player == other.next_player

    def __hash__(self):
        return hash((self.p1_pos, self.p2_pos, self.p1_score, self.p2_score, self.next_player))

dice_combinations = [[3, 1],
                     [4,3],
                     [5,6],
                     [6,7],
                     [7,6],
                     [8,3],
                     [9,1]]

known_states = dict()

def modulo_at_1(val, mod):
    modulo = val % mod
    return mod if modulo == 0 else modulo

def turn(pos, next_die_val):
    add = next_die_val + modulo_at_1(next_die_val+1,100) + modulo_at_1(next_die_val + 2, 100)
    new_pos = (pos + add)%10
    return modulo_at_1(new_pos, 10)

def wins_for_game_state(state):
    if state in known_states:
        return known_states[state]
    elif state.p1_score >= 21:
        res = [1,0]
    elif state.p2_score >= 21:
        res = [0,1]
    else:
        p1 = 0
        p2 = 0
        for v,m in dice_combinations:
            next_state_wins = wins_for_game_state(state.roll(v))
            p1 = p1+m*next_state_wins[0]
            p2 = p2+m*next_state_wins[1]
        res = [p1,p2]
    known_states[state] = res
    return res

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

    return min(p1_score, p2_score)*die_count

def puzzle2(data):
    p1_pos = int(data[0].split(": ")[-1])
    p2_pos = int(data[1].split(": ")[-1])
    start = State(p1_pos,p2_pos,0,0,1)

    [p1,p2] = wins_for_game_state(start)

    return max(p1,p2)

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))