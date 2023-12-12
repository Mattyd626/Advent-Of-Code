import math

def load_nodes(input):
    nodes = input[2:]
    node_dictionary = {}
    for node in nodes:
        [key, connections] = node.split(" = ")
        node_dictionary[key] = connections.split(", ")
        for i in range(len(node_dictionary[key])):
            node_dictionary[key][i] = node_dictionary[key][i].replace("(","")
            node_dictionary[key][i] = node_dictionary[key][i].replace(")","")
    return node_dictionary
        
def load_directions(input):
    directions = input[0]
    return directions

def part_1(input):
    nodes = load_nodes(input)
    directions = load_directions(input)
    position = "AAA"
    steps = 0
    found = False
    while not found:
        for direction in directions:
            position = nodes[position][0 if direction == "L" else 1]
            steps += 1
            if position == "ZZZ":
                found = True
                break
    return steps

def part_2(input):
    nodes = load_nodes(input)
    directions = load_directions(input)
    positions = []
    for node in nodes.keys():
        if node[-1] == "A":
            positions.append(node)
    
    def find_steps(position):
        steps = 0
        while True:
            for direction in directions:
                steps += 1
                position = nodes[position][0 if direction == "L" else 1]
                if position[-1] == "Z":
                    return steps
                
    steps = [find_steps(_) for _ in positions]
    return math.lcm(*steps)

if __name__ == "__main__":

    with open("2023/input8.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")