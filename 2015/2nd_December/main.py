def get_data():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    
    data = [[int(x) for x in line.strip().split("x")] for line in data]
    
    return data

if __name__ == "__main__":
    data = get_data()

    sum = 0
    for line in data:
        sum += 2 * line[0] * line[1] + 2 * line[1] * line[2] + 2 * line[0] * line[2]
        sum += min(line[0] * line[1], line[1] * line[2], line[0] * line[2])

    ribbon = 0

    for line in data:
        dims = sorted(line)

        ribbon += 2 * dims[0] + 2 * dims[1]
        ribbon += dims[0] * dims[1] * dims[2]

    print(ribbon)
          