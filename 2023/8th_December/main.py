def get_data(test=False) -> tuple:
    with open("data.txt", "r") as file:
        data = file.readlines()

    if not test:
        connections: dict = {}
        instructions: str = data[0].strip()

        for line in data[2:]:
            line = line.strip().split(" = ")
            connections[line[0]] = line[1].split(", ")

    else:
        instructions: str = "LR"
        connections: dict = {
            "11A": ("11B", "XXX"),
            "11B": ("XXX", "11Z"),
            "11Z": ("11B", "XXX"),
            "22A": ("22B", "XXX"),
            "22B": ("22C", "22C"),
            "22C": ("22Z", "22Z"),
            "22Z": ("22B", "22B"),
            "XXX": ("XXX", "XXX"),
        }

    return instructions, connections


def part_1(instructions: str, connections: dict) -> None:
    current_steps = 0
    current_position = "AAA"

    while True:
        if current_position == "ZZZ":
            print(f"Part 1: {current_steps}")
            break
        else:
            current_position = (
                connections[current_position][0]
                if instructions[current_steps % len(instructions)] == "L"
                else connections[current_position][1]
            )
            current_steps += 1


class Ghost:
    def __init__(self, position: str):
        self.position = position


def part_2(instructions: str, connections: dict) -> None:
    ghosts: list = []

    for connection in connections:
        if connection[-1] == "A":
            ghosts.append(Ghost(connection))

    cycles: list = [0 for _ in range(len(ghosts))]
    current_steps = 0
   
    while True:
        for index, ghost in enumerate(ghosts):
            if ghost.position[-1] == "Z":
                if cycles[index] == 0:
                    cycles[index] = current_steps

        finished = True
        for cycle in cycles:
            if cycle == 0:
                finished = False

        if not finished:
            for ghost in ghosts:
                if instructions[current_steps % len(instructions)] == "L":
                    ghost.position = connections[ghost.position][0]
                else:
                    ghost.position = connections[ghost.position][1]

            current_steps += 1
        
        else:
            import math

            print(f"Part 2 cycles: {cycles}")
            result = cycles[0]
            for num in cycles[1:]:
                result = abs(result * num) // math.gcd(result, num)

            print(f"Part 2 result: {result}")
            break


if __name__ == "__main__":
    instructions, connections = get_data(test=False)

    part_1(instructions, connections)

    part_2(instructions, connections)
