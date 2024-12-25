class crate_spot():
    def __init__(self, y, x):
        self.dist = 0
        self.x = x
        self.y = y
        self.weight = 1
        self.wall = False

    def find_neighbors(self, grid):
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


def get_bytes(bytes):
    with open("data.txt", "r") as file:
        data = file.readlines()
        return_data = []

        for i in range(bytes):
            return_data.append([int(data[i].split(",")[0]), int(data[i].split(",")[1])])

    return return_data


def get_test_data(bytes):
    data = ["5,4", "4,2", "4,5", "3,0", "2,1", "6,3", "2,4", "1,5", "0,6", "3,3", "2,6", "5,1", "1,2", "5,5", "2,5", "6,5", "1,4", "0,4", "6,4", "1,1", "6,1", "1,0", "0,5", "1,6", "2,0"]

    return_data = []

    for i in range(bytes):
        return_data.append([int(data[i].split(",")[0]), int(data[i].split(",")[1])])

    return return_data


def find_current_node(open_set):
    current = open_set[0]
    for node in open_set:
        if node.dist < current.dist:
            current = node
    return current


def dijkstra(grid, start, end):
    closed_set = []
    open_set = [start]
    current = start
        
    while current != end:
        if len(open_set) == 0:
            print("No path found")
            return False

        current = find_current_node(open_set)
        open_set.remove(current)
        closed_set.append(current)
        for i in range(len(current.neighbors)):
            neighbor = current.neighbors[i]
            if neighbor not in closed_set and not neighbor in open_set and not neighbor.wall:
                open_set.append(neighbor)
                neighbor.dist = current.dist + neighbor.weight
        
    return current.dist


def main():
    number_of_bytes = 1024
    width = 71

    data = get_bytes(number_of_bytes)

    grid = [[0 for i in range(width)] for j in range(width)]

    for i in range(width):
        for j in range(width):
            grid[i][j] = crate_spot(i, j)
    
    for i in range(width):
        for j in range(width):
            grid[i][j].find_neighbors(grid)
    
    for i in range(number_of_bytes):
        grid[data[i][1]][data[i][0]].wall = True

    shortest_path = dijkstra(grid, grid[0][0], grid[width-1][width-1])

    print(shortest_path)


def test():
    number_of_bytes = 12
    width = 7

    data = get_test_data(number_of_bytes)

    grid = [[0 for i in range(width)] for j in range(width)]

    for i in range(width):
        for j in range(width):
            grid[i][j] = crate_spot(i, j)
    
    for i in range(width):
        for j in range(width):
            grid[i][j].find_neighbors(grid)
    
    for i in range(number_of_bytes):
        grid[data[i][1]][data[i][0]].wall = True

    shortest_path = dijkstra(grid, grid[0][0], grid[width-1][width-1])

    print(shortest_path)


def part_2():
    width = 71


    for i in range(3451 - 1024):
        print(i)
        number_of_bytes = i + 1024
        data = get_bytes(number_of_bytes)

        grid = [[0 for i in range(width)] for j in range(width)]

        for i in range(width):
            for j in range(width):
                grid[i][j] = crate_spot(i, j)
        
        for i in range(width):
            for j in range(width):
                grid[i][j].find_neighbors(grid)
        
        for i in range(number_of_bytes):
            grid[data[i][1]][data[i][0]].wall = True

        shortest_path = dijkstra(grid, grid[0][0], grid[width-1][width-1])

        if not shortest_path:
            print(data[-1])
            break


if __name__ == "__main__":
    main()
    test()
    part_2()

