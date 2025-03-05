def get_data() -> tuple:
    with open("data.txt", "r") as file:
        data = file.readlines()

    winning_numbers: list = []
    our_numbers: list = []

    for line in data:
        list_to_append = []
        line_winning_numers = line[10:39].split(" ")

        for number in line_winning_numers:
            if number != "":
                list_to_append.append(int(number))

        winning_numbers.append(list_to_append)

        list_to_append = []
        line_our_numbers = line[42:118].split(" ")

        for number in line_our_numbers:
            if number != "":
                list_to_append.append(int(number))

        our_numbers.append(list_to_append)

    
    return winning_numbers, our_numbers

def get_test_data() -> tuple:
    our_numbers: list = [
        [83, 86, 6, 31, 17, 9, 48, 53],
        [61, 30, 68, 82, 17, 32, 24, 19],
        [69, 82, 63, 72, 16, 21, 14, 1],
        [59, 84, 76, 51, 58, 5, 54, 83],
        [88, 30, 70, 12, 93, 22, 82, 36],
        [74, 77, 10, 23, 35, 67, 36, 11]
    ]
    winning_numbers: list = [
        [41, 48, 83, 86, 17],
        [13, 32, 20, 16, 61],
        [1, 21, 53, 59, 44],
        [41, 92, 73, 84, 69],
        [87, 83, 26, 28, 32],
        [31, 18, 13, 56, 72]
    ]

    return winning_numbers, our_numbers


def part_1(winning_numbers, our_numbers) -> dict:
    total_score: int = 0
    card_scores: dict = {}

    for index, card in enumerate(our_numbers):
        card_score: int = 0
        correct_numbers: int = 0
        for number in card:
            if number in winning_numbers[index]:
                correct_numbers += 1
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2

        total_score += card_score
        card_scores[index] = correct_numbers

    print(total_score)
    return card_scores


def part_2(winning_numbers, our_numbers, card_scores) -> None:
    cards: dict = {}
    max_index: int = 215
   
    for i in range(len(our_numbers)):
        cards[i] = 1
    
    for card, score in card_scores.items():
        for i in range(score):
            if card+i+1 < max_index:
                cards[card+i+1] += 1 * cards[card]
    
    number_of_cards: int = 0

    for card in cards.values():
        number_of_cards += card

    print(number_of_cards)


if __name__ == "__main__":
    #winning_numbers, our_numbers = get_test_data()
    winning_numbers, our_numbers = get_data()

    card_scores = part_1(winning_numbers, our_numbers)

    part_2(winning_numbers, our_numbers, card_scores)
    