def get_values(fileInfo):
    data = {}
    symbols = []

    with open(fileInfo["file"]) as file:
        y = 0
        for line in file:
            line = line.replace("\n", "")
            current = ""
            for x in range(0, len(line)):
                if line[x].isnumeric():
                    current += line[x]
                elif current != "":
                    pos = (x - len(current), y) # start coordinates
                    data[pos] = current
                    current = ""
                if not line[x].isnumeric() and line[x] != ".":
                    symbols.append((x, y))

            # if we are at the end of the line...
            if current != "":
                pos = (x - len(current), y) # start coordinates
                data[pos] = current
            y += 1
    return (data, symbols)


def filter(data, symbols):
    filtered = []
    for d in data:
        found = False
        (x, y) = d
        for xi in range(x-1, x + len(data[d]) + 1):
            for yi in range(y-1, y+2):
                if (xi, yi) in symbols:
                    if d not in filtered:
                        filtered.append(d)

    result = []
    for pos in filtered:
        result.append(int(data[pos]))

    return result


def solve_part1(fileInfo):
    (data, symbols) = get_values(fileInfo)
    filtered = filter(data, symbols)
    return sum(filtered)


def solve_part2(fileInfo):
    return 0
