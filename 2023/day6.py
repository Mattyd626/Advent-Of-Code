def calculate_distance(time_held, race_duration):
    speed = time_held
    time_remaining = race_duration - time_held
    distance = speed * time_remaining
    return distance

def part_1(input):
    times = [int(_) for _ in input[0].split(":")[1].split(" ") if len(_) > 0]
    distances = [int(_) for _ in input[1].split(":")[1].split(" ") if len(_) > 0]
    total = 1
    for index in range(len(times)):
        wins = 0
        time = times[index]
        for i in range(time):
            if calculate_distance(i,time) > distances[index]:
                wins += 1
        total *= wins
    return total

def part_2(input):
    time = int("".join(input[0].split(":")[1].split(" ")))
    distance = int("".join(input[1].split(":")[1].split(" ")))
    start = 0
    end = 0
    for i in range(time):
        if calculate_distance(i,time) > distance:
            start = i
            break
    for i in range(time,0,-1):
        if calculate_distance(i,time) > distance:
            end = i
            break
    return end-start+1

if __name__ == "__main__":

    with open("2023/input6.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")