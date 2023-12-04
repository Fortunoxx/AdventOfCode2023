def get_values(fileInfo, part2=False):
    data = {}

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(":")
            card = int(parts[0].replace('Card ', ''))
            parts2 = parts[1].replace('  ', ' 0').split(" | ")
            data[card] = { "winning": parts2[0].split(' '), "numbers": parts2[1].split(' ') }
    return data


def calculate_winning_numbers(data):
    results = []
    for card_id in data:
        winning = data[card_id]["winning"]
        numbers = data[card_id]["numbers"]

        res = -1
        for n in numbers:
            if n in winning:
                res += 1
    
        if res >= 0:
            results.append(pow(2, res))
    return results


def solve_part1(fileInfo):
    data = get_values(fileInfo)
    result = calculate_winning_numbers(data)
    return sum(result)


def solve_part2(fileInfo):
    data = get_values(fileInfo)
    result = calculate_winning_numbers(data)
    return sum(result)
