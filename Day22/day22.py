from collections import defaultdict

class Cuboid:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

    def volume(self):
        return (1+self.x1-self.x0)*(1+self.y1-self.y0)*(1+self.z1-self.z0)

    def __getitem__(self, item):
        return [self.x0, self.x1, self.y0, self.y1, self.z0, self.z1][item]


def parse_cuboid(cuboid):
    op,coords = cuboid.split(' ')
    x_c,y_c,z_c = [[int(i) for i in coords.split(',')[a].split('=')[-1].split("..")] for a in range(3)]
    return op,Cuboid(x_c[0], x_c[1], y_c[0], y_c[1], z_c[0], z_c[1])

def calc_intersect(cuboid_a, cuboid_b):
    x_max_min = max(cuboid_a.x0, cuboid_b.x0)
    x_min_max = min(cuboid_a.x1, cuboid_b.x1)
    y_max_min = max(cuboid_a.y0, cuboid_b.y0)
    y_min_max = min(cuboid_a.y1, cuboid_b.y1)
    z_max_min = max(cuboid_a.z0, cuboid_b.z0)
    z_min_max = min(cuboid_a.z1, cuboid_b.z1)

    if x_max_min <= x_min_max and y_max_min <= y_min_max and z_max_min <= z_min_max:
        return Cuboid(x_max_min, x_min_max,y_max_min,y_min_max,z_max_min,z_min_max)
    else:
        return 0

def opposite_face(face):
    return face+1 if face%2==0 else face-1

def puzzle1(data):
    cubes = defaultdict(int)
    for line in data:
        op,coords = line.split(' ')
        x_c,y_c,z_c = [[int(i) for i in coords.split(',')[a].split('=')[-1].split("..")] for a in range(3)]
        if not (x_c[0]>50 or x_c[1]<-50 or y_c[0]>50 or y_c[1]<-50 or z_c[0]>50 or z_c[1]<-50):
            for x in range(max(-50,x_c[0]),min(51,x_c[1]+1)):
                for y in range(max(-50,y_c[0]),min(51,y_c[1]+1)):
                    for z in range(max(-50,z_c[0]),min(51,z_c[1]+1)):
                        if op == "on":
                            cubes[f'{x},{y},{z}'] = 1
                        else:
                            cubes[f'{x},{y},{z}'] = 0

    return sum(cubes.values())

def puzzle2(data):
    op,cuboid = parse_cuboid(data[0])
    on_cuboids = [cuboid]
    for line in data[1:]:
        op,cuboid = parse_cuboid(line)
        new_cuboids = []
        for c in on_cuboids:
            intersect = calc_intersect(c, cuboid)
            if intersect == 0:
                new_cuboids.append(c)
            else:
                sliced = []
                remaining = c
                faces = [f for f in range(6) if intersect[f]!=remaining[f]]
                for face in faces:
                    new_cuboid = Cuboid(*[remaining[i] if i!= opposite_face(face) else intersect[i-1]-1 if i%2==1 else intersect[i+1]+1 for i in range(6)])
                    sliced.append(new_cuboid)
                    remaining = Cuboid(*[remaining[i] if i!=face else intersect[i] for i in range(6)])
                new_cuboids.extend(sliced)
        if op == 'on':
            new_cuboids.append(cuboid)

        on_cuboids = list(new_cuboids)
    result = sum([c.volume() for c in on_cuboids])
    return result

if __name__ == '__main__':
    with open("input.txt") as file_stream:
        file = file_stream.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))