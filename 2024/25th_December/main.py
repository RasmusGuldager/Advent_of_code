def get_data(test):
    if not test:
        with open("data.txt") as file:
            data = file.readlines()
    else:
        with open("testdata.txt") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    schematics = []
    schematic = []

    for line in data:
            
        if line == "":
            schematics.append(schematic)
            schematic = []
            continue
                
        schematic.append(line)
    
    schematics.append(schematic)

    keys = []
    locks = []
        
    for schematic in schematics:
        if schematic[0] == "#####":
            locks.append(schematic)
        else:
            keys.append(schematic)

    key_coordinates = [[] for _ in range(len(keys))]
    lock_coordinates = [[] for _ in range(len(locks))]
        
    for key in range(len(keys)):
        for i in range(len(keys[key])):
            for j in range(len(keys[key][i])):
                if keys[key][i][j] == "#":
                    key_coordinates[key].append((i, j))
        
    for lock in range(len(locks)):
        for i in range(len(locks[lock])):
            for j in range(len(locks[lock][i])):
                if locks[lock][i][j] == "#":
                    lock_coordinates[lock].append((i, j))
        
    return key_coordinates, lock_coordinates
            
def main(key_coordinates, lock_coordinates):
    matches = 0

    for key in key_coordinates:
        for lock in lock_coordinates:
            for coordinate in range(len(key)):
                if key[coordinate] in lock:
                    break
                elif coordinate == len(key) - 1:
                    matches += 1
    
    print(matches)


if __name__ == "__main__":
    key_coordinates, lock_coordinates = get_data(test = False)

    main(key_coordinates, lock_coordinates)