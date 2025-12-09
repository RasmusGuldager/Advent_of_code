import re


def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    numbers = [line.strip("\n") for line in data[:-1]]
    operations = data[-1]

    return numbers, operations


def part_1(numbers, operations):
    total = 0

    numbers = [re.split(r"\s+", line.strip()) for line in numbers]
    operations = re.split(r"\s+", operations.strip())

    for i, operation in enumerate(operations):
        if operation == "+":
            answer = 0
        else:
            answer = 1

        for row in numbers:
            if operation == "+":
                answer += int(row[i])
            else:
                answer *= int(row[i])

        total += answer

    print("Part 1:", total)


def part_2(numbers, operations):
    total = 0

    operations = re.split(r"\s+", operations.strip())
    columns = [[] for _ in numbers[0]]

    for index in range(len(columns)):
        for row in numbers:
            columns[index].append(row[index])

    columns = ["".join(column) for column in columns]
    col_index = 0

    for i, operation in enumerate(operations):
        if operation == "+":
            answer = 0
        else:
            answer = 1

        while columns[col_index].strip() != "":
            number = int(columns[col_index].strip())

            if operation == "+":
                answer += number
            else:
                answer *= number

            col_index += 1

            if col_index == len(columns):
                break

        col_index += 1

        total += answer

    print("Part 2:", total)


if __name__ == "__main__":
    numbers, operations = get_data()

    part_1(numbers, operations)
    part_2(numbers, operations)
