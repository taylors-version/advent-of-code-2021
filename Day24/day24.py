import z3


def puzzle1(data):
    program = []
    for line in data:
        program.append(line.split())

    solver = z3.Optimize()
    digits = [z3.BitVec(f'd_{i}',64) for i in range(14)]

    for d in digits:
        solver.add(1 <= d)
        solver.add(d <= 9)
        digit_input = iter(digits)

    zero, one = z3.BitVecVal(0,64), z3.BitVecVal(1,64)

    registers = {r: zero for r in 'xyzw'}

    for i, inst in enumerate(program):
        if inst[0] == 'inp':
            registers[inst[1]] = next(digit_input)
            continue
        a,b = inst[1:]
        b = registers[b] if b in registers else int(b)
        c = z3.BitVec(f'v{i}', 64)
        if inst[0] == 'add':
            solver.add(c == registers[a] + b)
        elif inst[0] == 'mul':
            solver.add(c == registers[a] * b)
        elif inst[0] == 'mod':
            solver.add(registers[a] >= 0)
            solver.add(b>0)
            solver.add(c == registers[a]%b)
        elif inst[0] == 'div':
            solver.add(b != 0)
            solver.add(c == registers[a] / b)
        elif inst[0] == 'eql':
            solver.add(c == z3.If(registers[a] == b, one, zero))
        registers[a] = c

    solver.add(registers['z'] == 0)

    result = ""

    for f in (solver.maximize, solver.minimize):
        solver.push()
        f(sum((10 ** i) * d for i,d in enumerate(digits[::-1])))
        solver.check()
        m = solver.model()
        result = result + (''.join([str(m[d]) for d in digits])) + "\n"
        solver.pop()

    return result


if __name__ == '__main__':
    with open("input.txt") as file_stream:
        file = file_stream.read()
        print(puzzle1(file.splitlines()))