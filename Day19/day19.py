from itertools import groupby, combinations
import queue

scanner_locations = []
class Scanner:
    faces = [[[1,0,0],[0,1,0],[0,0,1]],
             [[1,0,0],[0,0,1],[0,-1,0]],
             [[1,0,0],[0,-1,0],[0,0,-1]],
             [[1,0,0],[0,0,-1],[0,1,0]],

             [[-1,0,0],[0,1,0],[0,0,-1]],
             [[-1,0,0],[0,0,1],[0,1,0]],
             [[-1,0,0],[0,-1,0],[0,0,1]],
             [[-1,0,0],[0,0,-1],[0,-1,0]],

             [[0,1,0],[1,0,0],[0,0,-1]],
             [[0,1,0],[0,0,1],[1,0,0]],
             [[0,1,0],[-1,0,0],[0,0,1]],
             [[0,1,0],[0,0,-1],[-1,0,0]],

             [[0,-1,0],[1,0,0],[0,0,1]],
             [[0,-1,0],[0,0,1],[-1,0,0]],
             [[0,-1,0],[-1,0,0],[0,0,-1]],
             [[0,-1,0],[0,0,-1],[1,0,0]],

             [[0,0,1],[1,0,0],[0,1,0]],
             [[0,0,1],[0,1,0],[-1,0,0]],
             [[0,0,1],[-1,0,0],[0,-1,0]],
             [[0,0,1],[0,-1,0],[1,0,0]],

             [[0,0,-1],[1,0,0],[0,-1,0]],
             [[0,0,-1],[0,1,0],[1,0,0]],
             [[0,0,-1],[-1,0,0],[0,1,0]],
             [[0,0,-1],[0,-1,0],[-1,0,0]]]

    def __init__(self, data):
        lines = [d.split(",") for d in data]
        self.beacons = [tuple(int(n) for n in l) for l in lines]
        ben = "hello"

    def all_rotations(self):
        return [[[sum([point[i] * b[i] for i in range(3)])
                       for point in [p for p in face]] for b in self.beacons]
                     for face in self.faces]


def accumulate(acc, x):
    if x == "":
        acc.append([])
    elif not x.startswith("--"):
        acc[-1].append(x)
    return acc

def get_matching(beacons, scanner):
    complete_map = set()

    for rotation in scanner.all_rotations():
        for known in beacons:
            for beacon in rotation:
                distance = (known[0]-beacon[0],known[1]-beacon[1],known[2]-beacon[2])
                matched = 0
                for b in rotation:
                    translated = (b[0]+distance[0],b[1]+distance[1],b[2]+distance[2])
                    complete_map.add(translated)
                    if translated in beacons:
                        matched+=1
                if matched >= 12:
                    complete_map.update(beacons)
                    scanner_locations.append(distance)
                    return complete_map
                complete_map.clear()
    return set()

def puzzle2(data):
    scanners = [Scanner(d) for k, d in groupby(data, key=lambda x: x == '' or x.startswith("--")) if not k]
    all_beacons = set()
    all_beacons.update(scanners[0].beacons)
    scanners_queue = queue.Queue()
    for s in scanners:
        scanners_queue.put(s)
    while not scanners_queue.empty():
        scanner = scanners_queue.get()
        is_matching = get_matching(all_beacons, scanner)
        if len(is_matching)==0:
            scanners_queue.put(scanner)
        else:
            all_beacons.update(is_matching)

    distances = [abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]) for a,b in combinations(scanner_locations, 2)]


    return f"Puzzle 1: {len(all_beacons)}\n Puzzle 2: {max(distances)}"


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle2(file.splitlines()))