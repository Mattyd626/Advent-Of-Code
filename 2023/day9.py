def part_1(input):
    ...

def part_2(input):
    ...

if __name__ == "__main__":

    with open("2023/input9.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")