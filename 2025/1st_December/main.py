def get_data(test=False):
    with open("data.txt", "r") as file:
        data = file.readlines()
    if test:
        with open("test_data.txt", "r") as file:
            data = file.readlines()
    return data


def part_1(data):
    number = 50
    password = 0

    for i in data:
        direction = i[0]
        distance = int(i[1:])

        number += distance if direction == "R" else -distance

        while number < 0:
            number += 100

        while number > 99:
            number -= 100

        if number == 0:
            password += 1

    print("part 1:", password)


def part_2(data):
    number = 50
    password = 0

    prev_num = number

    for i in data:
        direction = i[0]
        distance = int(i[1:])

        number += distance if direction == "R" else -distance

        password += abs(number // 100)
        number %= 100

        if direction == "L":
            if number == 0:
                password += 1

            if prev_num == 0:
                password -= 1


    prev_num = number

    print("part 2:", password)


if __name__ == "__main__":
    data = get_data()

    part_1(data)
    part_2(data)
