class Spot:
    def __init__(self, y, x):
        self.dist = 0
        self.x = x
        self.y = y
        self.wall = False
        self.prev = None
        self.direction = [0, 1]

    def get_neighbors(self, grid):
        self.neighbors = []
        if self.x > 0:
            self.neighbors.append(grid[self.y][self.x - 1])
        
        if self.x < len(grid) - 1:
            self.neighbors.append(grid[self.y][self.x + 1])
        
        if self.y > 0:
            self.neighbors.append(grid[self.y - 1][self.x])
        
        if self.y < len(grid[0]) - 1:
            self.neighbors.append(grid[self.y + 1][self.x])


def get_data():
    with open("data.txt", "r") as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    
    return data


def get_test_data():
    data = ["#################", "#...#...#...#..E#", "#.#.#.#.#.#.#.#.#", "#.#.#.#...#...#.#", "#.#.#.#.###.#.#.#", "#...#.#.#.....#.#", "#.#.#.#.#.#####.#", "#.#...#.#.#.....#", "#.#.#####.#.###.#", "#.#.#.......#...#", "#.#.###.#####.###", "#.#.#...#.....#.#", "#.#.#.#####.###.#", "#.#.#.........#.#", "#.#.#.#########.#", "#S#.............#", "#################"]
    
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


def find_current_node(open_set):
    current = open_set[0]
    for node in open_set:
        if node.dist < current.dist:
            current = node
    return current


def dijkstra(start, end):
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

        if current.dist > 78428:
            return 0, closed_set

        for i in range(len(current.neighbors)):
            neighbor = current.neighbors[i]
            
            if neighbor not in closed_set and not neighbor in open_set and not neighbor.wall:
                open_set.append(neighbor)
                neighbor.prev = current
                neighbor.direction = [abs(neighbor.y - current.y), abs(neighbor.x - current.x)]
                if neighbor.direction == current.direction:
                    neighbor.dist = current.dist + 1
                else:
                    neighbor.dist = current.dist + 1001

    return current.dist, closed_set


def main(grid, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = grid[i][j]
            elif data[i][j] == "E":
                end = grid[i][j]

    shortest_path, closed_set = dijkstra(start, end)

    print(f"Total cost of shortest path is {shortest_path}")

    is_on_path = 0

    list_of_nodes = []
    for i in range(len(closed_set)):
        list_of_nodes.append((closed_set[i], closed_set[i].dist))
    
    for i in range(len(closed_set)):
        print(100 * i // len(closed_set))

 
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid[x][y].dist = 0

        path_weight = dijkstra(list_of_nodes[i][0], end)[0]

        if path_weight + list_of_nodes[i][1] == shortest_path:
            is_on_path += 1

    print(f"Number of nodes on the shortest path is {is_on_path}") #451


if __name__ == '__main__':
    #data = get_data()
    data = get_test_data()

    grid = create_grid(data)

    main(grid, data)