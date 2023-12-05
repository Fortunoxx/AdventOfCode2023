def get_values(fileInfo):
    data = {}

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(":")
            card = int(parts[0].replace('Card ', ''))
            parts2 = parts[1].strip().replace('  ', ' 0').split(" | ")
            winning =  [int(n) for n in parts2[0].split(' ')]
            numbers =  [int(n) for n in parts2[1].split(' ')]
            data[card] = { "counter": 1, "winning": winning, "numbers": numbers }

    return data


def calculate_cards(data):
    for card_id in data:
        winning = data[card_id]["winning"]
        numbers = data[card_id]["numbers"]
        counter = data[card_id]["counter"]

        cnt = 0
        for n in numbers:
            if n in winning:
                cnt += 1

        for id in range(card_id + 1, card_id + 1 + cnt):
            data[id]["counter"] = data[id]["counter"] + counter

    return [data[processed]["counter"] for processed in data]


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
    result = calculate_cards(data)
    return sum(result)
