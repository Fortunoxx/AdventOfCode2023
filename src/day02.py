def get_values(fileInfo, part=1):
    values = {}

    with open(fileInfo["file"]) as file:
        for line in file:
            entries = []
            line = line.replace("\n", "")
            parts = line.split(": ")
            game = int(parts[0].split(" ")[1])

            draws = parts[1].split("; ")
            for draw in draws:
                colors = draw.split(", ")
                entry = {}
                for color in colors:
                    colorparts = color.split(" ")
                    entry[colorparts[1]] = int(colorparts[0])
                entries.append(entry)
            values[game] = entries
    return values


def get_compare_data():
    data = {}
    data["red"] = 12
    data["green"] = 13
    data["blue"] = 14
    return data


def get_valid_games(games, data):
    ids = []

    for game_id in games:
        valid = True
        for color in data:
            for item in games[game_id]:
                if color in item:
                    num = item[color]
                    if num > data[color]:
                        valid = False
                        break
            if not valid:
                break
        if valid:
            ids.append(game_id)

    return ids


def get_minimum_items(games):
    items = []
    
    for game_id in games:
        data = {}
        for game in games[game_id]:
            for key in game:
                if key not in data:
                    data[key] = game[key]
                elif data[key] < game[key]:
                    data[key] = game[key]

        items.append(data)

    return items


def get_powers(items):
    powers = []
    for i in items:
        power = 1
        for j in i:
            power *= i[j]
        powers.append(power)
    return powers


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    data = get_compare_data()
    ids = get_valid_games(values, data)
    return sum(ids)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    result = get_minimum_items(values)
    powers = get_powers(result)
    return sum(powers)
