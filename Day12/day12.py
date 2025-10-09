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
    queue = [["start", connection.other("start")] for connection in connections if "start" in connection]
    success = []
    while len(queue) != 0:
        for path in queue:
            queue.remove(path)
            if path[-1] == "end":
                success.append(path)
            else:
                for dest in [option.other(path[-1]) for option in connections if  path[-1] in option and option.other(path[-1]).lower() not in path]:
                    queue.append(path + [dest])

    return len(success)

def puzzle2(data):
    connections = [Connection(a,b) for [a,b] in [line.split("-") for line in data]]
    queue = [(["start", connection.other("start")], True) for connection in connections if "start" in connection]
    success = []
    while len(queue) != 0:
        for path in queue:
            queue.remove(path)
            if path[0][-1] == "end":
                success.append(path)
            else:
                for dest in [option.other(path[0][-1]) for option in connections if path[0][-1] in option and option.other(path[0][-1]) != "start"]:
                    if dest.lower() in path[0] and path[1]:
                        queue.append((path[0] + [dest], False))
                    elif dest.lower() not in path[0]:
                        queue.append((path[0] + [dest], path[1]))

    return len(success)

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))