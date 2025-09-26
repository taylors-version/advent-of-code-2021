class Connection:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __contains__(self, item):
        return item == self.a or item == self.b
    def other(self, start):
        return self.a if self.b == start else self.b

def puzzle1(data):
    connections = [Connection(a,b) for [a,b] in [line.split("-") for line in data]]
    queue = [[(connection, connection.other("start"))] for connection in connections if "start" in connection]
    success = []
    while len(queue) != 0:
        for path in queue:

            pass
    return 1

def puzzle2(data):
    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))