def part_1(input):
    sum = 0
    for card in input:
        score = 0.5
        [winning_numbers, numbers] = card.split(":")[1].split("|")
        winning_numbers = winning_numbers[1:-1].replace("  "," ").split(" ")
        numbers = numbers[1:].replace("  "," ").split(" ")

        for number in numbers:
            if number in winning_numbers:
                score *= 2
        
        if score > 0.5:
            sum += score
    
    return int(sum)

def part_2(input):
    wins = [0] * len(input)
    for index in range(len(input)):
        card = input[index]
        [winning_numbers, numbers] = card.split(":")[1].split("|")
        winning_numbers = winning_numbers[1:-1].replace("  "," ").split(" ")
        numbers = numbers[1:].replace("  "," ").split(" ")
        
        for number in numbers:
            if number in winning_numbers:
                wins[index] = wins[index] + 1
    
    def card_summer(cards, index):
        cards_won = cards[index]
        for i in range(cards[index]):
            if index+i+1 < len(cards):
                cards_won += card_summer(cards, index+i+1)
        return cards_won

    total = len(wins)

    for index in range(len(wins)):
        total += card_summer(wins, index)
    
    return total
if __name__ == "__main__":

    with open("2023/input4.txt",'r') as f:
        input = f.readlines()
        for index in range(len(input)):
            input[index] = input[index].strip()
        print(f"Part 1: {part_1(input)}")
        print(f"Part 2: {part_2(input)}")