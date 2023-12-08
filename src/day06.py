import re 

def get_values(fileInfo, is_part_2=False):
    data = {}
    key = "times"

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            items = []
    
            if is_part_2:
                items = [int(line.split(':')[1].replace(" ",""))]
            else:
                items = [int(n) for n in re.findall("\\d+", line.split(':')[1])]

            data[key] = items

            if key == "times":
                key = "distances"
            
    return data


def solve(data, is_part_2=False):
    all_results = {}
    for i in range(0, len(data["times"])):
        time = data["times"][i]
        dist = data["distances"][i]
        if is_part_2:
            all_results[i] = solve_time_dist_2(time, dist)
        else:
            all_results[i] = solve_time_dist(time, dist)
    return all_results


def solve_time_dist(time, dist):
    results = []
    for button_press_duration in range(0, time): # maybe optimize since 0 and time won't work at all
        time_left = time - button_press_duration
        result = calc_dist(button_press_duration, time_left)
        if result > dist:
            results.append(button_press_duration)
    return results


def solve_time_dist_2(time, dist):
    result_counter = 0
    for button_press_duration in range(0, time): # maybe optimize since 0 and time won't work at all
        time_left = time - button_press_duration
        result = calc_dist(button_press_duration, time_left)
        if result > dist:
            result_counter += 1
    return result_counter


def calc_dist(speed, time_left):
    return speed * time_left


def solve_part1(fileInfo):
    data = get_values(fileInfo)
    results = solve(data)
    total = 1
    for i in results:
        total *= len(results[i])
    return total


def solve_part2(fileInfo):
    data = get_values(fileInfo, True)
    results = solve(data, True)
    total = 1
    for i in results:
        total *= results[i]
    return total

