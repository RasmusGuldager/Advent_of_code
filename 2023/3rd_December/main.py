def get_data(test=False):
    if not test:
        with open("data.txt") as file:
            data = file.readlines()
    else:
        with open("testdata.txt") as file:
            data = file.readlines()

    data = [line.strip() for line in data]

    return data


def check_validity(indicies, data):
    symbols = "0123456789."

    for i in range(len(indicies)):
        try:
            if data[indicies[i][1]-1][indicies[i][0]] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]][indicies[i][0]-1] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]][indicies[i][0]+1] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]-1][indicies[i][0]-1] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]-1][indicies[i][0]+1] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]-1] not in symbols:
                return True
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]+1] not in symbols:
                return True
        except IndexError:
            pass
            
    return False


def check_gear(indicies, data):
    for i in range(len(indicies)):
        try:
            if data[indicies[i][1]-1][indicies[i][0]] == "*":
                return [indicies[i][1]-1, indicies[i][0]]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]] == "*":
                return [indicies[i][1]+1, indicies[i][0]]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]][indicies[i][0]-1] == "*":
                return [indicies[i][1], indicies[i][0]-1]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]][indicies[i][0]+1] == "*":
                return [indicies[i][1], indicies[i][0]+1]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]-1][indicies[i][0]-1] == "*":
                return [indicies[i][1]-1, indicies[i][0]-1]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]-1][indicies[i][0]+1] == "*":
                return [indicies[i][1]-1, indicies[i][0]+1]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]-1] == "*":
                return [indicies[i][1]+1, indicies[i][0]-1]
        except IndexError:
            pass
        try:
            if data[indicies[i][1]+1][indicies[i][0]+1] == "*":
                return [indicies[i][1]+1, indicies[i][0]+1]
        except IndexError:
            pass
            
    return False



def main(data):
    part_numbers = 0
    current_num = None
    current_num_indicies = []
    numbers = "0123456789"

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in numbers:
                if current_num != None:
                    current_num += data[i][j]
                else:
                    current_num = data[i][j]

                current_num_indicies.append([j, i])

            else:
                if current_num != None:
                    if check_validity(current_num_indicies, data):
                        part_numbers += int(current_num)

                    current_num = None
                    current_num_indicies = []

    print(part_numbers)

    # Part 2
    gear_ratio = 0
    current_num = None
    current_num_indicies = []
    gears = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in numbers:
                if current_num != None:
                    current_num += data[i][j]
                else:
                    current_num = data[i][j]

                current_num_indicies.append([j, i])
            
            else:
                if current_num != None:
                    if check_gear(current_num_indicies, data):
                        gears.append([current_num, check_gear(current_num_indicies, data)])

                    current_num = None
                    current_num_indicies = []

    for i in range(len(gears)):
        for j in range(i+1, len(gears)):
            if gears[i][1] == gears[j][1]:
                gear_ratio += int(gears[i][0]) * int(gears[j][0])
        
    print(gear_ratio)        


if __name__ == '__main__':
    data = get_data()
    main(data)
