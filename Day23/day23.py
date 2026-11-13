import copy
import math
import heapq


class State:
    available_hallway = [1,2,4,6,8,10,11]
    room_pos = {
        "a": 3,
        "b": 5,
        "c": 7,
        "d": 9
    }

    def __init__(self, energy):
        self.energy = energy
        self.hallway_blocked = {0,12}
        self.amphis = {}

    def set_amphi(self, amphi, place):
        if amphi in self.amphis and self.amphis[amphi].startswith("h"):
            self.hallway_blocked.remove(int(self.amphis[amphi][1:]))
        if place.startswith("h"):
            self.hallway_blocked.add(int(place[1:]))
        self.amphis[amphi] = place

    def parse(self, data):
        for i in [2,3]:
            for j in [3,5,7,9]:
                room = chr(96+j//2) + str(i-1)
                amphi = data[i][j]
                if amphi == 'A':
                    if "a0" not in self.amphis:
                        self.set_amphi("a0", room)
                    else:
                        self.set_amphi("a1", room)
                elif amphi == 'B':
                    if "b0" not in self.amphis:
                        self.set_amphi("b0", room)
                    else:
                        self.set_amphi("b1", room)
                elif amphi == 'C':
                    if "c0" not in self.amphis:
                        self.set_amphi("c0", room)
                    else:
                        self.set_amphi("c1", room)
                elif amphi == 'D':
                    if "d0" not in self.amphis:
                        self.set_amphi("d0", room)
                    else:
                        self.set_amphi("d1", room)
        for room in range(1,12):
            amphi = data[1][room]
            if amphi != '.':
                if amphi == 'A':
                    if "a0" not in self.amphis:
                        self.set_amphi("a0", "h"+str(room))
                    else:
                        self.set_amphi("a1", "h"+str(room))
                elif amphi == 'B':
                    if "b0" not in self.amphis:
                        self.set_amphi("b0", "h"+str(room))
                    else:
                        self.set_amphi("b1", "h"+str(room))
                elif amphi == 'C':
                    if "c0" not in self.amphis:
                        self.set_amphi("c0", "h"+str(room))
                    else:
                        self.set_amphi("c1", "h"+str(room))
                elif amphi == 'D':
                    if "d0" not in self.amphis:
                        self.set_amphi("d0", "h"+str(room))
                    else:
                        self.set_amphi("d1", "h"+str(room))

    def next_states(self):
        states = []
        for amphi,val in self.amphis.items():
            resolved = self.resolved_amphis()
            #Check it's not stuck behind another in its room and that it's not home already
            if (not (val[0]!="h" and val[1] == "2" and val[0]+"1" in self.amphis.values())
            and not val==amphi[0]+"2" and not amphi[0] in resolved):
                #Can it move to the hallway?
                if not val[0] == "h":
                    pos = State.room_pos[val[0]]
                    hallway_pos = self.get_hallway_places(pos)
                    for p in hallway_pos:
                        new_state = copy.deepcopy(self)
                        new_state.set_amphi(amphi,"h"+str(p))
                        energy_usage = math.pow(10,ord(amphi[0])-97)
                        new_state.energy = self.energy+energy_usage*(abs(pos-p)+int(val[1]))
                        states.append(new_state)
                #can it move to the room?
                x_pos = self.get_x_pos(val)
                #Check hallway route is empty and at least one space available
                empty_hallway = True
                dest_pos = int(State.room_pos[amphi[0]])
                for i in range(min(x_pos, dest_pos), max(x_pos, dest_pos)+1):
                    if "h"+str(i) in self.amphis.values() and self.amphis[amphi]!="h"+str(i):
                        empty_hallway = False
                if empty_hallway and not amphi[0]+"1" in self.amphis.values() and not amphi[0] in resolved:
                    if not amphi[0]+"2" in self.amphis.values():
                        #room totally free, can move into it (going down 2)
                        new_state = copy.deepcopy(self)
                        new_state.set_amphi(amphi, amphi[0]+"2")
                        distance = abs(x_pos-dest_pos)+2
                        if val[0]!="h":
                            distance = distance+int(val[1])
                        energy_usage = math.pow(10,ord(amphi[0])-97)
                        new_state.energy = self.energy+energy_usage*distance
                        states.append(new_state)
                    else:
                        other_amphi = amphi[0]+"1" if amphi[1]=="0" else amphi[0]+"0"
                        if self.amphis[other_amphi] == amphi[0]+"2":
                            #room totally free, can move into it (going down 1)
                            new_state = copy.deepcopy(self)
                            new_state.set_amphi(amphi, amphi[0]+"2")
                            distance = abs(x_pos-dest_pos)+1
                            if val[0]!="h":
                                distance = distance+int(val[1])
                            energy_usage = math.pow(10,ord(amphi[0])-97)
                            new_state.energy = self.energy+energy_usage*distance
                            states.append(new_state)
        return states

    def is_finished(self):
        complete = True
        for amphi,pos in self.amphis.items():
            if not pos.startswith(amphi[0]):
                complete = False
        return complete

    def resolved_amphis(self):
        resolved = []
        for amphi in ['a', 'b', 'c', 'd']:
            if ((self.amphis[amphi+"0"] == amphi+"1" and self.amphis[amphi+"1"] == amphi+"2")
                or (self.amphis[amphi+"1"] == amphi+"1" and self.amphis[amphi+"0"] == amphi+"2")):
                resolved.append(amphi)
        return resolved

    def get_hallway_places(self, pos):
        hallway_min = max([i for i in self.hallway_blocked if i < pos])
        hallway_max = min([i for i in self.hallway_blocked if i > pos])
        return [i for i in State.available_hallway if hallway_min < i < hallway_max]

    def get_x_pos(self, pos):
        if pos[0]=="h":
            return int(pos[1:])
        else:
            return State.room_pos[pos[0]]

    def __eq__(self, other):
        a_equal = (self.amphis["a0"]==other.amphis["a0"] and self.amphis["a1"]==other.amphis["a1"]) or (self.amphis["a0"]==other.amphis["a1"] and self.amphis["a1"]==other.amphis["a0"])
        b_equal = (self.amphis["b0"]==other.amphis["b0"] and self.amphis["b1"]==other.amphis["b1"]) or (self.amphis["b0"]==other.amphis["b1"] and self.amphis["b1"]==other.amphis["b0"])
        c_equal = (self.amphis["c0"]==other.amphis["c0"] and self.amphis["c1"]==other.amphis["c1"]) or (self.amphis["c0"]==other.amphis["c1"] and self.amphis["c1"]==other.amphis["c0"])
        d_equal = (self.amphis["d0"]==other.amphis["d0"] and self.amphis["d1"]==other.amphis["d1"]) or (self.amphis["d0"]==other.amphis["d1"] and self.amphis["d1"]==other.amphis["d0"])
        return a_equal and b_equal and c_equal and d_equal

    def __hash__(self):
        a_hash = hash(self.amphis["a0"])*hash(self.amphis["a1"])
        b_hash = hash(self.amphis["b0"])*hash(self.amphis["b1"])
        c_hash = hash(self.amphis["c0"])*hash(self.amphis["c1"])
        d_hash = hash(self.amphis["d0"])*hash(self.amphis["d1"])
        return hash((a_hash, b_hash, c_hash, d_hash))

    def __lt__(self, other):
        return self.energy < other.energy


def puzzle1(data):
    initial_state = State(0)
    initial_state.parse(data)
    queue = []
    settled_states = set()
    heapq.heappush(queue,initial_state)
    while queue:
        state = heapq.heappop(queue)
        if not state in settled_states:
            if state.is_finished():
                return state.energy
            more = state.next_states()
            for n in more:
                heapq.heappush(queue, n)

        settled_states.add(state)
        ben = "hi"
    return 0

def puzzle2(data):
    return 0

if __name__ == '__main__':
    with open("input.txt") as file_stream:
        file = file_stream.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))