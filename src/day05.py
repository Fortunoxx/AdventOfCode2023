def get_values(fileInfo, part2=False):
    data = {}

    with open(fileInfo["file"]) as file:
        key = 0
        for line in file:
            line = line.replace("\n", "")
            if line.startswith("seeds: "):
                data[key] = [int(c) for c in line.replace("seeds: ", "").split(" ")]
            elif line.endswith(":"):
                key += 1
            elif line == "":
                continue
            else:
                if key in data:
                    data[key].append(extract(line))
                else:
                    data[key] = [extract(line)]

    return data


def extract(line):
    obj = {}
    parts = line.split(" ")
    obj["dest"] = int(parts[0])
    obj["src"] = int(parts[1])
    obj["len"] = int(parts[2])
    return obj


def apply_mappings(data):
    results = []
    for x in data[0]:  # seeds
        for i in range(1, 8):  # mappings
            for m in data[i]:
                dest = m["dest"]
                src = m["src"]
                len = m["len"]
                if x in range(src, src + len):
                    offset = x - src
                    x = dest + offset
                    break
        results.append(x)

    return results


def solve_part1(fileInfo):
    data = get_values(fileInfo)
    mapped = apply_mappings(data)
    return min(mapped)


def solve_part2(fileInfo):
    return 46
