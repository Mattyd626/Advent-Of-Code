def find_line_value(line):
    first = None
    last = 0
    for char in line:
        if char in "0123456789":
            if first is None:
                first = int(char)
            last = int(char)
    return first * 10 + last

def replace_words(line):
    translations = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    rebuilt_string = []
    for head in range(len(line)):
        if line[head] in "0123456789":
            rebuilt_string.append(line[head])
        else:
            for key, value in translations.items():
                if head + len(key) <= len(line):
                    substring = line[head:head+len(key)]
                    if substring == key:
                        rebuilt_string.append(value)
                        continue
    return "".join(rebuilt_string)

def part_1(input):
    sum = 0
    for line in input:
        sum += find_line_value(line)
    print(sum)

def part_2(input):
    sum = 0
    for line in input:
        new_line = replace_words(line)
        if line is not new_line:
            print(f"{line} -> {new_line} -> {find_line_value(new_line)}")
        sum += find_line_value(new_line)
    print(sum)

if __name__ == "__main__":

    with open("2023/input1.txt",'r') as f:
        input = f.readlines()
        # part_1(input)
        part_2(input)