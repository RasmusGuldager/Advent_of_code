def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.read().strip().split(",")
    else:
        with open("test_data.txt", "r") as file:
            data = file.read().strip().split(",")

    data = [list(map(int, line.split("-"))) for line in data]
    
    return data


def part_1(data):
    invalid = 0

    for id_range in data:
        min = id_range[0]
        max = id_range[1]

        for i in range(min, max+1):
            temp = str(i)
            length = len(temp) // 2
            left = temp[0:length]
            right = temp[length:]

            if left == right:
                invalid += i

    print("Part 1:", invalid)



if __name__ == "__main__":
    data = get_data()

    part_1(data)
