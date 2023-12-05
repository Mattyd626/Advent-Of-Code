def load_map(input, map):
    found = False
    mappings = []
    for line in input:
        if not found:
            if map in line:
                found = True
        else:
            if len(line) == 0:
                break
            mappings.append([int(_) for _ in line.split(" ")])

    return mappings

def map_value(map, value):
    for mapping in map:
        if value >= mapping[1] and value < mapping[1] + mapping[2]:
            return value + mapping[0] - mapping[1]
    return value

# def combine_map(map1, map2):
#     overlap = True
#     current_map = [_ for _ in map1]
#     while overlap:
#         overlap = False
#         adjusted_map = []
#         for mapping_1 in current_map:
#             for mapping_2 in map2:
#                 if mapping_1[0] >= mapping_2[1] and mapping_1[0] < mapping_2[1] + mapping_2[2]: #Move source point to end of mapping 2 source + range
#                     if mapping_1[0] + mapping_1[2] < mapping_2[1] + mapping_2[2]: #mapping 1 is inside mapping 2, ignore
#                         overlap = True
#                     else: #mapping 1 is not inside so just move source to end of mapping 2 range
#                         new_source = mapping_2[1] + mapping_2[2]
#                         delta_range = new_source - mapping_1[1]
#                         adjusted_map.append([mapping_1[0]+delta_range,new_source,mapping_1[2]-delta_range])
#                         overlap = True
#                 elif mapping_2[1] >= mapping_1[0] and mapping_2[1] < mapping_1[0] + mapping_1[2]: #Move the source point to one before the source of mapping 2
#                     if mapping_2[1] + mapping_2[2] < mapping_1[0] + mapping_1[2]: #Mapping 2 is inside mapping 1, create two mappings either side
#                         new_source = mapping_2[1] + mapping_2[2] #create right side
#                         delta_range = new_source-mapping_1[1]
#                         adjusted_map.append([mapping_1[0]+delta_range,new_source,mapping_1[2]-delta_range])
#                         new_range = mapping_1[0]-mapping_2[1]
#                         adjusted_map.append([mapping_1[0],mapping_1[1],new_range])
#                         overlap = True
#                     else: #Mapping 1 is not inside, so reduce the range so that it is outside mapping 2 
#                         new_range = mapping_1[0]-mapping_2[1]
#                         adjusted_map.append([mapping_1[0],mapping_1[1],new_range])   
#                         overlap = True
#             if not overlap:
#                 adjusted_map.append(mapping_1)
#         current_map = [_ for _ in adjusted_map]
#         print(current_map)
#     current_map.extend(map2)
#     return current_map


            

def part_1(input):
    map_names = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    maps = {}
    for name in map_names:
        maps[name] = load_map(input, name)

    seeds = [int(_) for _ in input[0][7:].split(" ")]

    lowest = None

    for seed in seeds:
        value = seed
        for name in map_names:
            value = map_value(maps[name], value)
        if lowest is None or value < lowest:
            lowest = value
    return lowest

def part_2(input):
    map_names = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    maps = {}
    for name in map_names:
        maps[name] = load_map(input, name)

    seed_input = [int(_) for _ in input[0][7:].split(" ")]
    seeds = []
    for i in range(int(len(seed_input)/2)):
        seeds.append([seed_input[i*2], seed_input[i*2+1]])

    lowest = None

    count = 0
    for seed_range in seeds:
        for seed in range(seed_range[0],seed_range[0]+seed_range[1]):
            count = count + 1
            if count % 10000 == 0:
                print(f"{count/2217452483*100}%")
            value = seed
            for name in map_names:
                value = map_value(maps[name], value)
            if lowest is None or value < lowest:
                lowest = value
    return lowest


if __name__ == "__main__":

    with open("2023/input5.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")