def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    return data


def expand_universe(universe):
    rows_without_galaxy = [i for i in range(len(universe))]
    columns_without_galaxy = [j for j in range(len(universe[0]))]

    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                if i in rows_without_galaxy:
                    rows_without_galaxy.remove(i)
                if j in columns_without_galaxy:
                    columns_without_galaxy.remove(j)

    for row in reversed(rows_without_galaxy):
        universe.insert(row, ["."] * len(universe[0]))

    for column in reversed(columns_without_galaxy):
        for i in range(len(universe)):
            universe[i] = (
                "".join(universe[i][:column]) + "." + "".join(universe[i][column:])
            )

    return universe, rows_without_galaxy, columns_without_galaxy


def part_1(universe):
    # Find galaxies
    galaxies = []

    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append((i, j))

    # Find distances between all galaxy pairs
    distances = []

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance = abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
            distances.append(distance)

    print(f"Part 1: {sum(distances)}")


def part_2(universe, rows_without_galaxy, columns_without_galaxy):
    weight = 1000000

    galaxies = []

    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append((i, j))

    distances = []

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance = 0
            for x in range(
                min(galaxies[i][0], galaxies[j][0]) + 1,
                max(galaxies[i][0], galaxies[j][0]) + 1,
            ):
                if x in rows_without_galaxy:
                    distance += weight
                else:
                    distance += 1
            for y in range(
                min(galaxies[i][1], galaxies[j][1]) + 1,
                max(galaxies[i][1], galaxies[j][1]) + 1,
            ):
                if y in columns_without_galaxy:
                    distance += weight
                else:
                    distance += 1
            distances.append(distance)

    print(f"Part 2: {sum(distances)}")


if __name__ == "__main__":
    universe = get_data()
    expanded_universe, rows_without_galaxy, columns_without_galaxy = expand_universe(
        universe.copy()
    )

    part_1(expanded_universe)

    part_2(universe, rows_without_galaxy, columns_without_galaxy)
