import numpy as np

def get_data(test):
    with open("data.txt", "r") as file:
        if not test:
            return file.readlines()
        else:
            return ["RRRRIICCFF", "RRRRIICCCF", "VVRRRCCFFF", "VVRCCCJFFF", "VVVVCJJCFE", "VVIVCCJJEE", "VVIIICJJEE", "MIIIIIJJEE", "MIIISIJEEE", "MMMISSJEEE"]


def find_regions(letter):
    regions = []
    visited = []
    for i in range(len(letter)):
        for j in range(len(letter[i])):
            if [i, j] in visited:
                continue
            else:
                #The used algorithm is BFS
                if letter[i][j] == 1:
                    queue = [[i, j]]
                    region = [[i, j]]
                    visited.append([i, j])
                    while len(queue) > 0:
                        current = queue.pop(0)
                        if current[0] > 0:
                            if letter[current[0] - 1][current[1]] == 1 and [current[0] - 1, current[1]] not in visited:
                                queue.append([current[0] - 1, current[1]])
                                region.append([current[0] - 1, current[1]])
                                visited.append([current[0] - 1, current[1]])
                        if current[0] < len(letter) - 1:
                            if letter[current[0] + 1][current[1]] == 1 and [current[0] + 1, current[1]] not in visited:
                                queue.append([current[0] + 1, current[1]])
                                region.append([current[0] + 1, current[1]])
                                visited.append([current[0] + 1, current[1]])
                        if current[1] > 0:
                            if letter[current[0]][current[1] - 1] == 1 and [current[0], current[1] - 1] not in visited:
                                queue.append([current[0], current[1] - 1])
                                region.append([current[0], current[1] - 1])
                                visited.append([current[0], current[1] - 1])
                        if current[1] < len(letter[i]) - 1:
                            if letter[current[0]][current[1] + 1] == 1 and [current[0], current[1] + 1] not in visited:
                                queue.append([current[0], current[1] + 1])
                                region.append([current[0], current[1] + 1])
                                visited.append([current[0], current[1] + 1])
                    regions.append(region)

    
    return regions

def calculate_perimeter(region):
    perimeter = 0
    for i in range(len(region)):
        x = region[i][0]
        y = region[i][1]
          
        perimeter += [x, y - 1] not in region
        perimeter += [x, y + 1] not in region
        perimeter += [x - 1, y] not in region
        perimeter += [x + 1, y] not in region

    return perimeter

def count_sides(region):
    sides = 0
    for i in range(len(region)):
        x = region[i][0]
        y = region[i][1]


    return sides


def main():
    data = get_data(True)

    data = [i.strip() for i in data]

    letters = {}

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in letters:
                letters[data[i][j]] = np.zeros(len(data) * len(data[i])).reshape(len(data), len(data[i]))
            
            letters[data[i][j]][i][j] = 1
    
    price_part_1 = 0
    price_part_2 = 0

    for key in letters:
        regions = find_regions(letters[key])
        for region in regions:
            price_part_1 += len(region) * calculate_perimeter(region)
            price_part_2 += len(region) * count_sides(region)
    
    #print(price_part_1) # Answer is 1352976
    print(price_part_2) # Answer is 


if __name__ == "__main__":
    main()