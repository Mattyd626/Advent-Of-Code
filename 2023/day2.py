import re

def part_1(input):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    valid_games_sum = 0
    for game in input:
        valid = True
        [game_id, game_values] = game.split(":")
        game_values = [_.strip() for _ in re.split(",|;",game_values)]
        for value in game_values:
            [count, colour] = value.split(" ")
            if limits[colour] < int(count):
                valid = False
        if valid:
            valid_games_sum += int(game_id.split(" ")[1])
    return valid_games_sum

def part_2(input):
    power_sum = 0
    for game in input:
        [game_id, game_values] = game.split(":")
        game_values = [_.strip() for _ in re.split(",|;",game_values)]
        colour_mins = {
            "red": None,
            "blue": None,
            "green": None
        }
        for value in game_values:
            [count, colour] = value.split(" ")
            colour_mins[colour] = int(count) if colour_mins[colour] is None or colour_mins[colour] < int(count) else colour_mins[colour]
        power = 1
        for min in colour_mins.values():
            power *= min
        power_sum += power
    return power_sum

if __name__ == "__main__":

    with open("2023/input2.txt",'r') as f:
        input = f.readlines()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")