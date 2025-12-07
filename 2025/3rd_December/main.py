def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    return data


def part_1(data: list[str]) -> None:
    joltage = 0

    for bank in data:
        bank = [int(x) for x in bank]

        # Find max for first number
        first_num = max(bank[:-1])
        first_index = bank.index(first_num)

        # Find second number
        second_num = max(bank[first_index + 1 :])

        joltage += 10 * first_num + second_num

    print("Part 1:", joltage)


def part_2(data: list[str]) -> None:
    joltage = 0

    for bank in data:
        bank = [x for x in bank]

        while len(bank) > 12:
            max_num = "".join(bank[1:])
            pop_index = 0

            for i in range(1, len(bank)):
                temp = "".join(bank[:i]) + "".join(bank[i + 1 :])
                if temp > max_num:
                    max_num = temp
                    pop_index = i

            bank.pop(pop_index)

        joltage += int("".join([str(x) for x in bank]))

    print("Part 2:", joltage)


if __name__ == "__main__":
    data = get_data()

    part_1(data)
    part_2(data)
