def check_index(point):
    if point[0] < 0 or point[0] >= len(data):
        return False
    
    if point[1] < 0 or point[1] >= len(data[0]):
        return False
    
    return True

with open('data.txt') as file:
    data = file.readlines()
    data = [i.strip() for i in data]
    
    frequencies = {}

    antinode_indices = []
    antinode_indices_part_2 = []
    antinode = [0, 0]

    # Test data
    #data = ["............", "........0...", ".....0......", ".......0....", "....0.......", "......A.....", "............", "............", "........A...", ".........A..", "............", "............"]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in frequencies:
                if data[i][j] != '.':
                    frequencies[data[i][j]] = [[i, j]]
                    antinode_indices_part_2.append([i, j].copy())

            else:
                frequencies[data[i][j]].append([i, j])
                antinode_indices_part_2.append([i, j].copy())


    for key in frequencies:
        for i in range(len(frequencies[key])):
            for j in range(1, len(frequencies[key])):
                if i < j:
                    antinode[0] = frequencies[key][i][0] - (frequencies[key][j][0] - frequencies[key][i][0])
                    if frequencies[key][i][1] > frequencies[key][j][1]:
                        antinode[1] = frequencies[key][i][1] + (frequencies[key][i][1] - frequencies[key][j][1])
                    
                    elif frequencies[key][i][1] < frequencies[key][j][1]:
                        antinode[1] = frequencies[key][i][1] - (frequencies[key][j][1] - frequencies[key][i][1])

                    else:
                        antinode[1] = frequencies[key][i][1]

                    if check_index(antinode):
                        if antinode not in antinode_indices:
                            antinode_indices.append(antinode.copy())
                            #print(antinode, frequencies[key][i], frequencies[key][j])

                    antinode[0] = frequencies[key][j][0] + (frequencies[key][j][0] - frequencies[key][i][0])
                    if frequencies[key][i][1] > frequencies[key][j][1]:
                        antinode[1] = frequencies[key][j][1] - (frequencies[key][i][1] - frequencies[key][j][1])
                    
                    elif frequencies[key][i][1] < frequencies[key][j][1]:
                        antinode[1] = frequencies[key][j][1] + (frequencies[key][j][1] - frequencies[key][i][1])

                    else:
                        antinode[1] = frequencies[key][i][1]
                   
                    if check_index(antinode):
                        if antinode not in antinode_indices:
                            antinode_indices.append(antinode.copy())
                            #print(antinode, frequencies[key][i], frequencies[key][j])

    
    #print(len(antinode_indices)) # The answer is 222
    
    for key in frequencies:
        for i in range(len(frequencies[key])):
            for j in range(1, len(frequencies[key])):
                if i < j:
                    k = 1
                    while True:
                        antinode[0] = frequencies[key][i][0] - (frequencies[key][j][0] - frequencies[key][i][0]) * k
                        if frequencies[key][i][1] > frequencies[key][j][1]:
                            antinode[1] = frequencies[key][i][1] + (frequencies[key][i][1] - frequencies[key][j][1]) * k
                        
                        elif frequencies[key][i][1] < frequencies[key][j][1]:
                            antinode[1] = frequencies[key][i][1] - (frequencies[key][j][1] - frequencies[key][i][1]) * k

                        else:
                            antinode[1] = frequencies[key][i][1]

                        if check_index(antinode):
                            k += 1
                            if antinode not in antinode_indices_part_2:
                                antinode_indices_part_2.append(antinode.copy())
                                #print(antinode, frequencies[key][i], frequencies[key][j])
                        else:
                            break


                    k = 1
                    while True:
                        antinode[0] = frequencies[key][j][0] + (frequencies[key][j][0] - frequencies[key][i][0]) * k
                        if frequencies[key][i][1] > frequencies[key][j][1]:
                            antinode[1] = frequencies[key][j][1] - (frequencies[key][i][1] - frequencies[key][j][1]) * k
                        
                        elif frequencies[key][i][1] < frequencies[key][j][1]:
                            antinode[1] = frequencies[key][j][1] + (frequencies[key][j][1] - frequencies[key][i][1]) * k

                        else:
                            antinode[1] = frequencies[key][i][1]
                    
                        if check_index(antinode):
                            k += 1
                            if antinode not in antinode_indices_part_2:
                                antinode_indices_part_2.append(antinode.copy())
                                #print(antinode, frequencies[key][i], frequencies[key][j])
                        else:
                            break  
                    

    print(len(antinode_indices_part_2)) # The answer is over 884            