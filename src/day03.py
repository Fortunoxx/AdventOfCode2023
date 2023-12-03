def get_values(fileInfo, part2=False):
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
                
                if not line[x].isnumeric() or x == (len(line) - 1):
                    if current != "":
                        pos = (x - len(current), y) # start coordinates
                        data[pos] = current
                        current = ""

                if part2:
                    if line[x] == "*":
                        symbols.append((x, y))
                elif not line[x].isnumeric() and line[x] != ".":
                    symbols.append((x, y))

            y += 1
    return (data, symbols)


def filter2(data, symbols):
    filtered = {}
    for d in data:
        (x, y) = d
        for xi in range(x-1, x + len(data[d]) + 1):
            for yi in range(y-1, y+2):
                pos = (xi, yi)
                if pos in symbols:
                    if pos not in filtered:
                        filtered[pos] = [data[d]]
                    else:
                        filtered[pos].append(data[d])

    result = []
    for f in filtered:
        items = filtered[f]
        if len(items) == 2:
            result.append(int(items[0]) * int(items[1]))

    return result


def filter(data, symbols):
    filtered = []
    for d in data:
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
    (data, symbols) = get_values(fileInfo, True)
    filtered = filter2(data, symbols)
    return sum(filtered)
