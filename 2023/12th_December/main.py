import itertools

def get_data(test=False):
    if test:
        with open("test_data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    rows = []
    groups = []

    for line in data:
        line = line.split(" ")
        rows.append(line[0])
        groups.append([int(x) for x in line[1].split(",")])

    return rows, groups


def check_validity(row, group):
    checked_group = []
    length = 0
    for i in range(len(row)):
        if row[i] == ".":
            if length > 0:
                checked_group.append(length)
            length = 0
        else:
            length += 1
    
    if length > 0:
        checked_group.append(length)

    return checked_group == group


def part_1(rows, groups):
    arrangements = []

    for index, row in enumerate(rows):
        arrangements_for_row = 0

        jokers = [i for i, char in enumerate(row) if char == "?"]
        combinations = itertools.product(["#", "."], repeat=len(jokers))

        for combo in combinations:
            new_row = list(row)
            for i, char in zip(jokers, combo):
                new_row[i] = char

            if check_validity(new_row, groups[index]):
                arrangements_for_row += 1
        
        arrangements.append(arrangements_for_row)

    print(f"Part 1: {sum(arrangements)}")
        
    
if __name__ == "__main__":
    rows, groups = get_data()

    part_1(rows, groups)
