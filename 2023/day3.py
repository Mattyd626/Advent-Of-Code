

def part_1(input):
    for index in range(len(input)):
        input[index] = input[index].strip()
    width = len(input[0])
    height =  len(input)
    valid_map = [False]*width*height

    for y in range(height):
        for x in range(width):
            if input[y][x] not in ".0123456789":
                for x1 in range(-1,2):
                    for y1 in range(-1,2):
                        if x + x1 > -1 and x + x1 < width and y + y1 > -1 and y + y1 < height:
                            valid_map[x+x1+(y+y1)*width] = True
    
    valid_sum = 0
    number = ""
    number_valid = False
    for y in range(height):
        for x in range(width):
            if input[y][x] in "0123456789":
                number = number + input[y][x]
                if valid_map[x+y*width]:
                    number_valid = True
            elif number_valid:
                valid_sum += int(number)
                number_valid = False
                number = ""
            else:
                number = ""
    return valid_sum


def part_2(input):
    for index in range(len(input)):
        input[index] = input[index].strip()
    width = len(input[0])
    height =  len(input)
    number_map = [[0]]*width*height

    number = ""
    for y in range(height):
        for x in range(width):
            if input[y][x] in "0123456789":
                number = number + input[y][x]
            elif len(number) > 0:
                for x1 in range(-len(number),0):
                    number_map[x+x1+y*width] = [int(number),f"{x},{y}"]        
                number = ""
            else:
                number = ""

    ratio_sum = 0
    for y in range(height):
        for x in range(width):
            if input[y][x] == "*":
                gear_ratio = 1
                count = 0
                neighbours = []
                for x1 in range(-1,2):
                    for y1 in range(-1,2):
                            if number_map[x+x1+(y+y1)*width][0] > 0 and number_map[x+x1+(y+y1)*width][1] not in neighbours:
                                neighbours.append(number_map[x+x1+(y+y1)*width][1])
                                count += 1
                                gear_ratio *= number_map[x+x1+(y+y1)*width][0]
                if count == 2:
                    ratio_sum += gear_ratio
    return ratio_sum

if __name__ == "__main__":

    with open("2023/input3.txt",'r') as f:
        input = f.readlines()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")