class Spot():
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.dist = 99999999
        self.wall = False
        self.prev = None
        self.index = None

    def get_neighbors(self, grid):
        neighbors = []
        if self.x > 0:
            neighbors.append(grid[self.y][self.x - 1])
        if self.x < len(grid) - 1:
            neighbors.append(grid[self.y][self.x + 1])
        if self.y > 0:
            neighbors.append(grid[self.y - 1][self.x])
        if self.y < len(grid) - 1:
            neighbors.append(grid[self.y + 1][self.x])

        self.neighbors = neighbors


def get_data():
    with open("data.txt", "r") as file:
        data = file.readlines()

        data = [line.strip() for line in data]
    
    return data

def get_test_data():
    data = ["###############", "#...#...#.....#", "#.#.#.#.#.###.#", "#S#...#.#.#...#", "#######.#.#.###", "#######.#.#...#", "#######.#.###.#", "###..E#...#...#", "###.#######.###", "#...###...#...#", "#.#####.#.###.#", "#.#...#.#.#...#", "#.#.#.#.#.#.###", "#...#...#...###", "###############"]

    return data

def create_grid(data):
    grid = [[0 for i in range(len(data[j]))] for j in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[i][j] = Spot(i, j)
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[i][j].get_neighbors(grid)

            if data[i][j] == "#":
                grid[i][j].wall = True

    return grid
            

def find_path(grid, start, end):
    open_set = [start]
    closed_set = []
    start.dist = 0

    while len(open_set) > 0:
        current = open_set[0]
        open_set.remove(current)
        closed_set.append(current)

        for neighbor in current.neighbors:
            if neighbor not in closed_set and not neighbor.wall and neighbor not in open_set:
                open_set.append(neighbor)
            
            if current.dist + 1 < neighbor.dist:
                neighbor.dist = current.dist + 1
                neighbor.prev = current
        
        if current == end:
            print("Path found")
            path = []
            current = end

            while current is not None:
                path.append(current)
                current = current.prev
           
            path.reverse()

            for i in range(len(path)):
                path[i].index = i

            return path
    
    print("No path found")
    return False


def find_cheats(grid, i, j):
    if i > 0 and i < len(grid) - 2:
        if grid[i-1][j].index is not None and grid[i+1][j].index is not None:
            if abs(grid[i-1][j].index - grid[i+1][j].index) > 1:
                return True
            
    if j > 0 and j < len(grid[i]) - 2:
        if grid[i][j-1].index is not None and grid[i][j+1].index is not None:
            if abs(grid[i][j-1].index - grid[i][j+1].index) > 1:
                return True

    return False


def find_cheats_part_2(grid, i, j):
    if grid[i][j].index is not None:
        cheats = 0
        for x in range(-20, 21):
            for y in range(-20, 21):
                if abs(x) + abs(y) <= 20:    
                    if 0 <= i + y < len(grid) and 0 <= j + x < len(grid[i]):
                        if grid[i+y][j+x].index is not None:
                            if (grid[i+y][j+x].index - grid[i][j].index) - (abs(x) + abs(y)) >= 100:
                                cheats += 1

        return cheats


def main(grid, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = grid[i][j]
            elif data[i][j] == "E":
                end = grid[i][j]

    normal_path = find_path(grid, start, end)

    print(f"Normal path length is {len(normal_path)}")

    possible_cheats = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].wall:
                possible_cheats += find_cheats(grid, i, j)
    
    print(f"Possible cheats are {possible_cheats}")

    possible_cheats_part_2 = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j].wall:
                possible_cheats_part_2 += find_cheats_part_2(grid, i, j)
    
    print(f"Possible cheats in part 2 are {possible_cheats_part_2}")


if __name__ == '__main__':
    data = get_data()
    #data = get_test_data()  
    grid = create_grid(data)
    
    main(grid, data)

