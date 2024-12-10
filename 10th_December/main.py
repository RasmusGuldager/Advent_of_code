import sys

def check_neighbours(index, num):
    try:
        if data[index[0] + 1][index[1]] == num + 1 and not [index[0] + 1, index[1]] in visited:
            return [1, 0]
    except:
        pass

    try:
        if data[index[0]][index[1] + 1] == num + 1 and not [index[0], index[1] + 1] in visited:
            return [0, 1]
    except:
        pass

    try:
        if data[index[0] - 1][index[1]] == num + 1 and not [index[0] - 1, index[1]] in visited:
            return [-1, 0]
    except:
        pass
    
    try: 
        if data[index[0]][index[1] - 1] == num + 1 and not [index[0], index[1] - 1] in visited:
            return [0, -1]
    except:
        pass

    return False


def find_path(index, num):
    global total_score
    print(current_path)
    if check_neighbours(index, num):
        visited.append(index.copy())
        current_path.append(index.copy())
        return find_path([index[0] + check_neighbours(index, num)[0], index[1] + check_neighbours(index, num)[1]], num + 1)

    else:
        if num == 9:
            total_score += 1
            visited.append(index.copy())
            
        
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
    data = ["89010123", "78121874", "87430965", "96549874", "45678903", "32019012", "01329801", "10456732"]
    
    data = [[int(d) for d in data[i]] for i in range(len(data))]

    current_path = []

    total_score = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            current_path = []
            if not data[i][j] == 0:
                continue

            else:
                visited = []
                find_path([i, j], 0)


    
    print(total_score)
