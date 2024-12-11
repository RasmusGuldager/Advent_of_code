import sys

def check_neighbours(index, num):
    neightbours = []
    try:
        if data[index[0] + 1][index[1]] == num + 1 and [index[0] + 1, index[1]] not in visited:
            neightbours.append([1, 0])
    except:
        pass

    try:
        if data[index[0]][index[1] + 1] == num + 1 and [index[0], index[1] + 1] not in visited:
            neightbours.append([0, 1])
    except:
        pass

    try:
        if data[index[0] - 1][index[1]] == num + 1 and [index[0] - 1, index[1]] not in visited and index[0] - 1 >= 0:
            neightbours.append([-1, 0])
    except:
        pass
    
    try: 
        if data[index[0]][index[1] - 1] == num + 1 and [index[0], index[1] - 1] not in visited and index[1] - 1 >= 0: 
            neightbours.append([0, -1])
    except:
        pass

    return neightbours[0] if neightbours else False


def find_path(index, num):
    global total_score
    print(current_path)
    neighbour = check_neighbours(index, num)
    if neighbour:
        visited.append([index[0] + neighbour[0], index[1] + neighbour[1]])
        current_path.append([index[0] + neighbour[0], index[1] + neighbour[1]])
        return find_path([index[0] + neighbour[0], index[1] + neighbour[1]], num + 1)

    else:
        if num == 9:
            total_score += 1
            
        
        current_path.pop(-1)
        #print(check_neighbours(current_path[-1], num - 1), current_path[-1], visited)
        if current_path:
            return find_path(current_path[-1], num - 1)
        else:
            return False

        

with open("data.txt", "r") as file:
    sys.setrecursionlimit(10000)
    data = file.readlines()

    data = [line.strip() for line in data]

    # Test data
    #data = ["89010123", "78121874", "87430965", "96549874", "45678903", "32019012", "01329801", "10456732"]
    
    data = [[int(d) for d in data[i]] for i in range(len(data))]

    current_path = []

    total_score = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not data[i][j] == 0:
                continue

            else:
                current_path = [[i, j]]
                visited = []
                find_path([i, j], 0)


    
    print(total_score) # Answer is 782