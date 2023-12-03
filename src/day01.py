def get_values(fileInfo, part=1):
    entries = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if part == 2:
                line = convert_text_to_numbers(line)
            entries.append(get_numeric_values(line))
    return calc_sum(entries)


def calc_sum(entries):
    sum = 0
    for entry in entries:
        if len(entry) > 1:
            sum += int(entry[0]) * 10 + int(entry[len(entry) - 1])
        elif len(entry) == 1:
            sum += int(entry[0]) * 10 + int(entry[0])
    return sum


def get_numeric_values(line):
    chars = []
    for char in line:
        if char.isnumeric():
            chars.append(int(char))
    return chars


def convert_text_to_numbers(line):
    items = [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]

    digits = []
    for i in range(0, len(line)):
        part = line[-(len(line)-i):]
        for (key, value) in items:
            if part.startswith(key):
                digits.append(value)
                break
            elif part.startswith(str(value)):
                digits.append(value)
                break
    
    new = ""
    for d in digits:
        new += str(d)    
    return new
                



def solve_part1(fileInfo):
    return get_values(fileInfo)


def solve_part2(fileInfo):
    return get_values(fileInfo, 2)
