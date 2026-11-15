import copy
import math
import heapq
import datetime


class Room:
    def __init__(self, room_size, name):
        self.stack = []
        self.room_size = room_size
        self.name = name

    def __eq__(self, other):
        return self.name==other.name and self.stack==other.stack

    def __hash__(self):
        return hash((self.name,self.stack))

    def push(self, amphi):
        self.stack.append(amphi)

    def pop(self):
        if len(self.stack) == 0:
            return "Error"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Error"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def has_others(self):
        if self.size() == 0:
            return False
        for amphi in self.stack:
            if amphi != self.name:
                return True
        return False

    def is_complete(self):
        return self.size() == self.room_size and not self.has_others()




class State:
    available_hallway = [1,2,4,6,8,10,11]
    room_pos = {
        "A": 3,
        "B": 5,
        "C": 7,
        "D": 9
    }

    def __init__(self, energy, room_size):
        self.energy = energy
        self.room_size = room_size
        self.hallway = ['S','.','.','.','.','.','.','.','.','.','.','.','E']#Put values in start and end to make logic easier
        self.rooms = {"A": Room(room_size, "A"),
                      "B": Room(room_size, "B"),
                      "C": Room(room_size, "C"),
                      "D": Room(room_size, "D")}


    def add_to_room(self, room, amphi):
        self.rooms[room].push(amphi)

    def remove_from_room(self, room):
        self.rooms[room].pop()

    def next_states(self):
        for e,i in zip(self.hallway,range(len(self.hallway))):
            if e != '.' and e != 'S' and e != 'E':
                """check if room is available"""
                if not self.rooms[e].has_others():
                    """check pathway is clear"""
                    dest_pos = State.room_pos[e]
                    min_pos = min(i+1,dest_pos)
                    max_pos = max(i,dest_pos)
                    if all([self.hallway[h] == '.' for h in range(min(i+1,dest_pos), max(i,dest_pos))]):
                        """move into room"""
                        new_state = copy.deepcopy(self)
                        new_state.hallway[i]='.'
                        new_state.rooms[e].push(e)
                        distance = self.room_size-self.rooms[e].size()+abs(dest_pos-i)
                        energy_usage = math.pow(10,ord(e)-65)
                        new_state.energy = self.energy + energy_usage*distance
                        return [new_state]

        """check each room for if they can receive"""
        for room in self.rooms.values():
            if not room.has_others() and not room.is_complete():
                """check if one of "room" is at the top"""
                for r in [r for r in self.rooms.values() if r != room]:
                    if r.peek()==room.name:
                        """check hallway is clear"""
                        start_pos = State.room_pos[room.name]
                        dest_pos = State.room_pos[r.name]
                        if all(h == "." for h in range(min(start_pos, dest_pos), max(start_pos, dest_pos))):
                            """move into room"""
                            new_state = copy.deepcopy(self)
                            new_state.rooms[room.name].pop()
                            new_state.rooms[r.name].push(r.name)
                            distance = 1+self.room_size-room.size() + 1+self.room_size-r.size()+abs(dest_pos-start_pos)
                            energy_usage = math.pow(10,ord(room.name)-65)
                            new_state.energy = self.energy + energy_usage*distance
                            return [new_state]
        """Can't move into a room, so collecting possible hallway moves"""
        states = []
        for name,room in self.rooms.items():
            if room.has_others():
                start_pos = State.room_pos[name]
                """lowend = 1 + first non-dot looking left from room_pos else 1"""
                """highend = -1 + first non-dot looking right from room_pos else 11"""
                min_pos = 1+max(i for i in range(0,start_pos) if self.hallway[i]!='.')
                max_pos = min(i for i in range(start_pos, 13) if self.hallway[i]!='.')
                for h in [h for h in range(min_pos, max_pos) if h in State.available_hallway]:
                    """move into hall position"""
                    new_state = copy.deepcopy(self)
                    amphi = new_state.rooms[name].pop()
                    new_state.hallway[h] = amphi
                    distance = 1+self.room_size-room.size() + abs(start_pos - h)
                    energy_usage = math.pow(10,ord(amphi)-65)
                    new_state.energy = self.energy + energy_usage*distance
                    states.append(new_state)

        return states

    def is_finished(self):
       return all([r.is_complete() for r in self.rooms.values()])


    def __eq__(self, other):
        return self.rooms==other.rooms and self.hallway == other.hallway

    def __hash__(self):
        rooms_hash = 1
        for room in self.rooms:
            rooms_hash = rooms_hash * room.__hash__()
        return hash((rooms_hash,tuple(self.hallway)))

    def __lt__(self, other):
        return self.energy < other.energy

def solver(data, size):
    initial_state = State(0, size)
    for i in range(1+size,1,-1):
        for j in [3,5,7,9]:
            room = chr(64+j//2)
            if data[i][j]!='.':
                initial_state.add_to_room(room, data[i][j])
    for i in range(1,12):
        initial_state.hallway[i]=data[1][i]

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
    return 0


def puzzle1(data):
    return solver(data,2)

def puzzle2(data):
    data.insert(3, "  #D#B#A#C#  ")
    data.insert(3, "  #D#C#B#A#  ")
    return solver(data,4)

if __name__ == '__main__':
    with open("input.txt") as file_stream:
        file = file_stream.read()
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(puzzle1(file.splitlines()))
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(puzzle2(file.splitlines()))
        print(now.strftime("%Y-%m-%d %H:%M:%S"))