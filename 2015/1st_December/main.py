def get_data():
    with open("data.txt", "r") as file:
        data = file.read()
    return data


if __name__ == "__main__":

    data = get_data()

    floor: int = 0

    for symbol in data:
        if symbol == "(":
            floor += 1
        elif symbol == ")":
            floor -= 1

    print(floor)
    floor = 0

    for i, symbol in enumerate(data):
        if symbol == "(":
            floor += 1
        elif symbol == ")":
            floor -= 1

        if floor == -1:
            print(i + 1)
            break
