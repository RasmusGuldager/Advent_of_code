def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    return data


class Spot:
    def __init__(self, x, y, paper) -> None:
        self.x: int = x
        self.y: int = y
        self.paper: bool = paper
        self.paper_neighbors: int

    def find_neighbors(self, grid):
        self.paper_neighbors = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        max_x = len(grid)
        max_y = len(grid[0])

        for dx, dy in directions:
            nx = self.x + dx
            ny = self.y + dy

            if 0 <= nx < max_x and 0 <= ny < max_y:
                self.paper_neighbors += grid[ny][nx].paper


def create_grid(data):
    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

    # Create spots
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[y][x] = Spot(x, y, data[y][x] == "@")

    # Find neighbors
    for y in range(max_y):
        for x in range(max_x):
            grid[y][x].find_neighbors(grid)

    return grid


def part_1(grid):
    accessible_paper = 0

    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x].paper:
                if grid[y][x].paper_neighbors < 4:
                    accessible_paper += 1

    print("Part 1:", accessible_paper)


def part_2(grid):
    accessible_paper = 0
    paper_removed = 1

    while paper_removed > 0:
        paper_removed = 0
        for y in range(max_y):
            for x in range(max_x):
                grid[y][x].find_neighbors(grid)

        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x].paper:
                    if grid[y][x].paper_neighbors < 4:
                        accessible_paper += 1
                        paper_removed += 1
                        grid[y][x].paper = False

    print("Part 2:", accessible_paper)


if __name__ == "__main__":
    data = get_data()

    global max_x
    max_x = len(data[0])

    global max_y
    max_y = len(data)

    grid = create_grid(data)

    part_1(grid)
    part_2(grid)
