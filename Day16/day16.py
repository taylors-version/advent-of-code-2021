from functools import reduce
from operator import mul


class Version:
    def __init__(self, data):
        self.version = int(data,2)

class Type:
    def __init__(self, data):
        self.id = int(data, 2)

class Package:
    def __init__(self, data):
        self.packages = []
        self.size = 0
        self.val = 0
        index = 0
        self.version = Version(data[:index + 3]).version
        index += 3
        self.type_id = Type(data[index:index + 3]).id
        index +=3
        if self.type_id == 4:
            binary = []
            while data[index] == "1":
                new_data = data[index+1:index+5]
                binary.extend(new_data)
                index += 5
            binary.extend(data[index+1:index+5])
            index +=5
            self.val = int("".join(binary), 2)
        else:
            if data[index] == "0":
                index +=1
                length = int(data[index:index+15],2)
                index +=15
                used = 0
                while used < length:
                    package = Package(data[index:index+(length-used)])
                    self.packages.append(package)
                    used += package.size
                    index += package.size
            else:
                index += 1
                sub_packages = int(data[index:index+11],2)
                index +=11
                while  len(self.packages) < sub_packages:
                    package = Package(data[index:])
                    self.packages.append(package)
                    index += package.size
        self.size = index

    def score(self):
        return self.version + sum(s.score() for s in self.packages)

    def value(self):
        values = [s.value() for s in self.packages]
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return reduce(mul, values)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 4:
            return self.val
        elif self.type_id == 5:
            if self.packages[0].value() > self.packages[1].value():
                return 1
            return 0
        elif self.type_id == 6:
            if self.packages[0].value() < self.packages[1].value():
                return 1
            return 0
        else:
            if self.packages[0].value() == self.packages[1].value():
                return 1
            return 0



def puzzle1(data):
    binary = "".join([bin(int(d,16))[2:].zfill(4) for d in data])
    package = Package(binary)

    return package.score()

def puzzle2(data):
    binary = "".join([bin(int(d,16))[2:].zfill(4) for d in data])
    package = Package(binary)

    return package.value()

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))