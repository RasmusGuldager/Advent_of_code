def get_data(test=False) -> tuple:
    with open("data.txt", "r") as file:
        data = file.readlines()

    if not test:
        hands = []
        bids = []

        for line in data:
            line = line.strip().split(" ")
            hands.append(line[0])
            bids.append(int(line[1]))

    else:
        hands = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
        bids = [765, 684, 28, 220, 483]

    return hands, bids


def order_hands(hands: list) -> dict:
    hands_dict = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
    }

    rank_map = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    for hand in hands:
        hand_type = rank_hand(hand)
        hands_dict[hand_type].append(hand)

    for key in hands_dict:
        hands_dict[key] = sorted(
            hands_dict[key], key=lambda x: [rank_map.index(card) for card in x]
        )

    return hands_dict


def order_hands_jokers(hands: list) -> dict:
    hands_dict = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_a_kind": [],
        "full_house": [],
        "four_of_a_kind": [],
        "five_of_a_kind": [],
    }

    rank_map = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    hands_rankings = [
        "high_card",
        "one_pair",
        "two_pair",
        "three_of_a_kind",
        "full_house",
        "four_of_a_kind",
        "five_of_a_kind",
    ]

    for hand in hands:
        if "J" in hand:
            best_hand: str = "high_card"
            for card in rank_map:
                hand_copy = hand.replace("J", card)
                hand_copy_type = rank_hand(hand_copy)
                if hands_rankings.index(hand_copy_type) > hands_rankings.index(
                    best_hand
                ):
                    best_hand = hand_copy_type

        else:
            best_hand = rank_hand(hand)

        hands_dict[best_hand].append(hand)

    for key in hands_dict:
        hands_dict[key] = sorted(
            hands_dict[key], key=lambda x: [rank_map.index(card) for card in x]
        )

    return hands_dict


def rank_hand(hand: str) -> str:
    hand_count = {card: hand.count(card) for card in set(hand)}

    if 5 in hand_count.values():
        return "five_of_a_kind"
    elif 4 in hand_count.values():
        return "four_of_a_kind"
    elif 3 in hand_count.values() and 2 in hand_count.values():
        return "full_house"
    elif 3 in hand_count.values():
        return "three_of_a_kind"
    elif list(hand_count.values()).count(2) == 2:
        return "two_pair"
    elif 2 in hand_count.values():
        return "one_pair"
    else:
        return "high_card"


def calculate_winnings(ordered_hands: dict, pairs: dict) -> None:
    rank: int = 1
    winnings: int = 0

    for key in ordered_hands:
        for hand in ordered_hands[key]:
            winnings += rank * pairs[hand]
            rank += 1

    print(f"Total winnings: {winnings}")


if __name__ == "__main__":
    hands, bids = get_data()

    pairs = {}
    for index, hand in enumerate(hands):
        pairs[hand] = bids[index]

    ordered_hands = order_hands(hands)

    ordered_hands_with_jokers = order_hands_jokers(hands)

    calculate_winnings(ordered_hands, pairs)

    calculate_winnings(ordered_hands_with_jokers, pairs)
