

def puzzle1(data):
    right = set()
    down = set()
    x_size = len(data[0])
    y_size = len(data)

    for y in range(y_size):
        for x in range(x_size):
            if data[y][x] == ">":
                right.add((x,y))
            elif data[y][x] == "v":
                down.add((x,y))

    count = 1
    while True:
        new_right = set()
        new_down = set()

        for (x,y) in right:
            testing = ((x+1) % x_size,y)
            if testing not in right and testing not in down:
                new_right.add(testing)
            else:
                new_right.add((x,y))
        for (x,y) in down:
            testing = (x, (y+1) % y_size)
            if testing not in new_right and testing not in down:
                new_down.add(testing)
            else:
                new_down.add((x,y))

        if new_right == right and new_down == down:
            return count

        right = new_right
        down = new_down
        count = count + 1
        #print(count)

    ben = "hi"

    return 0

def puzzle2(data):
    return "Happy Christmas"

if __name__ == '__main__':
    with open("input.txt") as file_stream:
        file = file_stream.read()
        print(puzzle1(file.splitlines()))
        print(puzzle2(file.splitlines()))