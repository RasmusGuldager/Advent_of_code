def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip().split(",") for line in data]

    return data


def part_1(data):
    max_size = 0

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = int(data[i][0]), int(data[i][1])
            x2, y2 = int(data[j][0]), int(data[j][1])

            size = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if size > max_size:
                max_size = size

    print("Part 1:", max_size)


if __name__ == "__main__":
    data = get_data()

    part_1(data)
