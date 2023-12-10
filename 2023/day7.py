

def part_1(input):
    character_strength = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12
    }

    def get_character_strength(character):
        return character_strength[character]

    def get_hand_type(hand):
        character_counts = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "T": 0,
            "J": 0,
            "Q": 0,
            "K": 0,
            "A": 0
        }
        for character in hand:
            character_counts[character] += 1
        sum = [_ for _ in character_counts.values() if _ > 0]
        sum.sort(reverse=True)
        if sum[0] == 5:
            return 6
        elif sum[0] == 4:
            return 5
        elif sum[0] == 3 and sum[1] == 2:
            return 4
        elif sum[0] == 3:
            return 3
        elif sum[0] == 2 and sum[1] == 2:
            return 2
        elif sum[0] == 2:
            return 1
        return 0

    def compare_hands(hand_1,hand_2):
        type_1 = get_hand_type(hand_1)
        type_2 = get_hand_type(hand_2)
        if type_1 > type_2:
            return 0
        elif type_1 < type_2:
            return 1
        
        for i in range(5):
            strength_1 = get_character_strength(hand_1[i])
            strength_2 = get_character_strength(hand_2[i])
            if strength_1 > strength_2:
                return 0
            elif strength_1 < strength_2:
                return 1
        
        return None

    hands_and_bids = [_.split(" ") for _ in input]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(hands_and_bids)-1):
            if compare_hands(hands_and_bids[i][0], hands_and_bids[i+1][0]) == 0:
                temp = hands_and_bids[i]
                hands_and_bids[i] = hands_and_bids[i+1]
                hands_and_bids[i+1] = temp
                sorted = False
    sum = 0
    for i in range(len(hands_and_bids)):
        sum += (i+1) * int(hands_and_bids[i][1])
    return sum

def part_2(input):
    character_strength = {
        "J": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "T": 9,
        "Q": 10,
        "K": 11,
        "A": 12
    }
    def get_character_strength(character):
        return character_strength[character]

    def get_hand_type(hand):
        character_counts = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "T": 0,
            "J": 0,
            "Q": 0,
            "K": 0,
            "A": 0
        }
        for character in hand:
            character_counts[character] += 1
        j_count = character_counts.pop("J")
        sum = [_ for _ in character_counts.values() if _ > 0]
        sum.sort(reverse=True)
        if j_count == 5:
            return 6
        if sum[0] + j_count == 5:
            return 6
        elif sum[0] + j_count == 4:
            return 5
        elif (sum[0] == 3 and sum[1] + j_count == 2) or (sum[0] == 2 and sum[1] + j_count == 3):
            return 4
        elif sum[0] + j_count == 3:
            return 3
        elif (sum[0] == 2 and sum[1] + j_count == 2):
            return 2
        elif sum[0] + j_count == 2:
            return 1
        return 0

    def compare_hands(hand_1,hand_2):
        type_1 = get_hand_type(hand_1)
        type_2 = get_hand_type(hand_2)
        if type_1 > type_2:
            return 0
        elif type_1 < type_2:
            return 1
        
        for i in range(5):
            strength_1 = get_character_strength(hand_1[i])
            strength_2 = get_character_strength(hand_2[i])
            if strength_1 > strength_2:
                return 0
            elif strength_1 < strength_2:
                return 1
        
        return None

    hands_and_bids = [_.split(" ") for _ in input]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(hands_and_bids)-1):
            if compare_hands(hands_and_bids[i][0], hands_and_bids[i+1][0]) == 0:
                temp = hands_and_bids[i]
                hands_and_bids[i] = hands_and_bids[i+1]
                hands_and_bids[i+1] = temp
                sorted = False
    sum = 0
    for i in range(len(hands_and_bids)):
        sum += (i+1) * int(hands_and_bids[i][1])
    return sum


if __name__ == "__main__":

    with open("2023/input7.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")