import numpy as np


with open("data.txt", "r") as file:
    data = file.read()
    data = list(data)
    data = [int(i) for i in data]

    # Test data
    #data = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]

    number_of_bytes = sum(data)

    disk = np.zeros(number_of_bytes)
    write_index = 0
    check_sum = 0
    read_index = len(disk) - 1

    for i in range(len(data)):
        for j in range(data[i]):
            if i % 2 == 0:
                disk[write_index] = i / 2
            else:
                disk[write_index] = -1
            write_index += 1

    empty_indices = np.where(disk == -1)

    for i in range(len(empty_indices[0])):
        for j in range(read_index, 0, -1):
            if disk[j] != -1 and empty_indices[0][i] < j:
                disk[empty_indices[0][i]] = disk[j]
                disk[j] = -1
                read_index = j
                break

    for i in range(len(disk)):
        if disk[i] == -1:
            break
        check_sum += disk[i] * i

    print(check_sum)

         

