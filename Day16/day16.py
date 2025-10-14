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
        index = 0
        self.version = Version(data[:index + 3]).version
        index += 3
        type_id = Type(data[index:index + 3]).id
        index +=3
        if type_id == 4:
            while data[index] == "1":
                index += 5
            index +=5
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



def puzzle1(data):
    binary = "".join([bin(int(d,16))[2:].zfill(4) for d in data])
    package = Package(binary)

    return package.score()

def puzzle2(data):

    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file))
        print(puzzle2(file))