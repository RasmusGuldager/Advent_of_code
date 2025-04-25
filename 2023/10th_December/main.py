import math


def get_data(test=False):
    with open("data.txt", "r") as file:
        data = file.readlines()

    if test:
        data = [
            "FF7FSF7F7F7F7F7F---7",
            "L|LJ||||||||||||F--J",
            "FL-7LJLJ||||||LJL-77",
            "F--JF--7||LJLJ7F7FJ-",
            "L---JF-JLJ.||-FJLJJ7",
            "|F|F-JF---7F7-L7L|7|",
            "|FFJF7L7F-JF7|JL---7",
            "7-L-JL7||F7|L7F-7F7|",
            "L.L7LFJ|||||FJL7||LJ",
            "L7JLJL-JLJLJL--JLJ.L",
        ]

    else:
        for index, line in enumerate(data):
            data[index] = line.strip()

    return data


class Spot:
    def __init__(self, y, x, icon):
        self.x = x
        self.y = y
        self.prev = None
        self.icon = icon
        self.visited = False
        self.in_path = False
        self.distance = 0
        self.neighbors = []

    def find_neighbors(self, grid):
        if self.y > 0 and (
            self.icon == "|" or self.icon == "J" or self.icon == "L" or self.icon == "S"
        ):
            self.neighbors.append(grid[self.y - 1][self.x])
        if self.y < len(grid) - 1 and (
            self.icon == "|" or self.icon == "F" or self.icon == "7" or self.icon == "S"
        ):
            self.neighbors.append(grid[self.y + 1][self.x])
        if self.x > 0 and (
            self.icon == "-" or self.icon == "J" or self.icon == "7" or self.icon == "S"
        ):
            self.neighbors.append(grid[self.y][self.x - 1])
        if self.x < len(grid[0]) - 1 and (
            self.icon == "-" or self.icon == "F" or self.icon == "L" or self.icon == "S"
        ):
            self.neighbors.append(grid[self.y][self.x + 1])


def setup(data):
    grid = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    for index1, row in enumerate(data):
        for index2, icon in enumerate(row):
            grid[index1][index2] = Spot(index1, index2, icon)
            if icon == "S":
                start = grid[index1][index2]

    for index1, row in enumerate(grid):
        for index2, spot in enumerate(row):
            spot.find_neighbors(grid)

    for index1, row in enumerate(grid):
        for index2, spot in enumerate(row):
            for neighbor in spot.neighbors:
                if spot not in neighbor.neighbors:
                    spot.neighbors.remove(neighbor)

    return grid, start


def pathfinding(start):
    current = start
    path = []
    start.neighbors.pop(1)

    while current:
        #print(f"Current: {current.icon} ({current.x}, {current.y})")
        current.visited = True
        unvisited_neighbors = []

        for neighbor in current.neighbors:
            if neighbor.icon == "S" and current.distance > 1:
                print(f"Furthest distance: {math.ceil(current.distance / 2)}")
                
                while current.prev:
                    current.in_path = True
                    path.append(current)
                    current = current.prev
                
                return path

            if not neighbor.visited:
                neighbor.distance = current.distance + 1
                neighbor.prev = current
                unvisited_neighbors.append(neighbor)

        if unvisited_neighbors:
            current = unvisited_neighbors[0]


def main(grid, start):
    path = pathfinding(start)

    spots_inside_loop = 0

    for row in grid:
        inside = False
        for spot in row:
            if spot.icon in "|JLS" and spot.visited:
                inside = not inside
            elif inside and not spot.visited:
                spots_inside_loop += 1

    print(f"Spots inside loop: {spots_inside_loop}")



if __name__ == "__main__":
    data = get_data()
    grid, start = setup(data)

    main(grid, start)
