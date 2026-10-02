import itertools
from functools import reduce

image_size = 0

def process(lit, iea, iteration):
    processed = set()
    new_lit = set()

    for (y,x) in itertools.product(range(0-iteration,image_size+1+iteration),range(0-iteration,image_size+1+iteration)):
        bin_string = ""
        for dy,dx in itertools.product(range(-1,2), range(-1,2)):
            compare_point = (x+dx, y+dy)
            if compare_point in lit or (iea[0]=='#' and iteration % 2 == 0 and (compare_point[0] < 0-iteration or compare_point[0] > (image_size-1) + iteration or compare_point[1] < 0-iteration or compare_point[1] > (image_size-1) + iteration)):
                bin_string = bin_string + "1"
            else:
                bin_string = bin_string + "0"
        n = int(bin_string, 2)
        if iea[n] == '#':
            new_lit.add((x,y))

    #for (x,y) in lit:
    #    for y_diff,x_diff in itertools.product(range(-1,2), range(-1,2)):
    #        point = (x+x_diff, y+y_diff)
    #        if point not in processed:
    #            processed.add(point)
    #            bin_string = ""
    #            for dy,dx in itertools.product(range(-1,2), range(-1,2)):
    #                compare_point = (point[0]+dx, point[1]+dy)
    #                if compare_point in lit or (iea[0]=='#' and iteration % 2 == 0 and (compare_point[0] < 0-iteration or compare_point[0] > (image_size-1) + iteration or compare_point[1] < 0-iteration or compare_point[1] > (image_size-1) + iteration)):
    #                    bin_string = bin_string + "1"
    #                else:
    #                    bin_string = bin_string + "0"
    #            n = int(bin_string, 2)
    #            if iea[n] == '#':
    #                new_lit.add(point)

    return new_lit

def puzzle1(data):
    iea = data[0]
    image = data[2:]
    global image_size
    image_size = len(image)

    lit = reduce(lambda x,y: x+y,
                 [[(x,y) for x in range(len(image[0])) if image[y][x] == '#']
                  for y in range(len(image))])
    print(f"list: {len(lit)}")
    for i in range(2):
        lit = process(lit, iea, i+1)
        print(f"list: {len(lit)}")

    return len(lit)

def puzzle2(data):
    return 0


if __name__ == '__main__':
    with open("input.txt") as f:
        file = f.read()
        print(puzzle1(file.splitlines())) #5223 <-> 5324 too high not 5293
        print(puzzle2(file.splitlines()))