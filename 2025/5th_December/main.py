def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    ranges = []
    ingredients = []

    for line in data:
        if "-" in line:
            ranges.append([int(x) for x in line.strip().split("-")])
        else:
            ingredients.append(int(line.strip()))

    return ranges, ingredients


def part_1(ranges, ingredients):
    good_ingredients = 0

    for ingredient in ingredients:
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                good_ingredients += 1
                break

    print("Part 1:", good_ingredients)


def part_2(ranges):
    fresh_ids = 0
    prev_ranges = []

    for id_range in ranges:
        new_range = True
        new_ranges = []
        l, r = id_range[0], id_range[1]

        for prev_range in prev_ranges:
            # Totally inside prev_range
            if prev_range[0] <= l and r <= prev_range[1]:
                new_range = False
                new_ranges.append(prev_range)
                continue

            # prev_range range totally inside
            if prev_range[0] >= l and r >= prev_range[1]:
                continue

            if prev_range[0] <= l <= prev_range[1]:
                l = prev_range[1] + 1

            elif prev_range[0] <= r <= prev_range[1]:
                r = prev_range[0] - 1

            new_ranges.append(prev_range)

        if new_range and l <= r:
            new_ranges.append([l, r])
            print("Added range:", id_range)

        prev_ranges = new_ranges

    for range in prev_ranges:
        fresh_ids += 1 + range[1] - range[0]

    print("Part 2:", fresh_ids)


if __name__ == "__main__":
    ranges, ingredients = get_data(False)

    part_1(ranges, ingredients)
    part_2(ranges)
