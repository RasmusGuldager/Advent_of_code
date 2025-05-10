def get_data():
    with open("data.txt", "r") as file:
        data = file.read()
    return data


if __name__ == "__main__":
    data = get_data()

    location: list = [0, 0]
    visited_locations = [location.copy()]

    for move in data:
        if move == "^":
            location[0] -= 1
        elif move == "v":
            location[0] += 1
        elif move == "<":
            location[1] -= 1
        elif move == ">":
            location[1] += 1
        else:
            print(f"Error: {move}")
        if location not in visited_locations:
            visited_locations.append(location.copy())

    print(len(visited_locations))

    # Part 2
    santa_location: list = [0, 0]
    elf_location: list = [0, 0]
    visited_locations = [santa_location.copy()]

    for index, move in enumerate(data):
        if index % 2:
            if move == "^":
                santa_location[0] -= 1
            elif move == "v":
                santa_location[0] += 1
            elif move == "<":
                santa_location[1] -= 1
            elif move == ">":
                santa_location[1] += 1
            else:
                print(f"Error: {move}")

            if santa_location not in visited_locations:
                visited_locations.append(santa_location.copy())

        else:
            if move == "^":
                elf_location[0] -= 1
            elif move == "v":
                elf_location[0] += 1
            elif move == "<":
                elf_location[1] -= 1
            elif move == ">":
                elf_location[1] += 1
            else:
                print(f"Error: {move}")

            if elf_location not in visited_locations:
                visited_locations.append(elf_location.copy())

    print(len(visited_locations))
