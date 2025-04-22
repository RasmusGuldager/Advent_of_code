def get_data(test=False):
    with open("data.txt", "r") as file:
        data = file.readlines()

    if not test:
        histories = []
        for line in data:
            histories.append([int(x) for x in line.strip().split(" ")])

    else:
        histories = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]

    return histories


def part_1(histories):
    last_numbers = 0

    for history in histories:
        sequences = [history]

        while sequences[-1].count(0) != len(sequences[-1]):
            sequences.append(generate_next_row(sequences[-1]))

        number_to_add = 0
        for sequence in reversed(sequences):
            sequence.append(sequence[-1] + number_to_add)
            number_to_add = sequence[-1]

        last_numbers += number_to_add

    print(f"Part 1: {last_numbers}")


def part_2(histories):
    first_numbers = 0

    for history in histories:
        sequences = [history]

        while sequences[-1].count(0) != len(sequences[-1]):
            sequences.append(generate_next_row(sequences[-1]))

        for index, sequence in enumerate(reversed(sequences)):
            if index == 0:
                last_sequence = sequence
                sequence.append(0)
            else:
                num_to_insert = sequence[0] - last_sequence[0]
                sequence.insert(0, num_to_insert)

                last_sequence = sequence

        first_numbers += num_to_insert

    print(f"Part 2: {first_numbers}")


def generate_next_row(row):
    new_row = [0] * (len(row) - 1)

    for index, num in enumerate(row):
        if index == 0:
            continue
        else:
            new_row[index - 1] = row[index] - row[index - 1]

    return new_row


if __name__ == "__main__":
    histories = get_data()

    part_1(histories)
    part_2(histories)
