def get_data():
    with open("data.txt") as file:
        data = file.readlines()
        data = [line.strip().split("-") for line in data]

        for i in range(len(data)):
            data[i].sort()

    return data

def get_test_data():
    data = ["kh-tc", "qp-kh", "de-cg", "ka-co", "yn-aq", "qp-ub", "cg-tb", "vc-aq", "tb-ka", "wh-tc", "yn-cg", "kh-ub", "ta-co", "de-co", "tc-td", "tb-wq", "wh-td", "ta-ka", "td-qp", "aq-cg", "wq-ub", "ub-vc", "de-ta", "wq-aq", "wq-vc", "wh-yn", "ka-de", "kh-ta", "co-tc", "wh-qp", "tb-vc", "td-yn"]

    data = [line.strip().split("-") for line in data]

    for i in range(len(data)):
        data[i].sort()

    return data

def part_1(data):
    connected_sets = []

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sets_with_t = 0

    for index, line in enumerate(data):
        print(index*100 // len(data))
        for x in alphabet:
            for y in alphabet:
                if sorted([f"{x}{y}", line[0]]) in data and sorted([f"{x}{y}", line[1]]) in data:   
                    if sorted([f"{x}{y}", line[0], line[1]]) not in connected_sets:
                        connected_sets.append(sorted([f"{x}{y}", line[0], line[1]]))
    
    for i in connected_sets:
        for j in i:
            if j[0] == "t":
                sets_with_t += 1
                break

    print(sets_with_t)


def part_2(data):
    connections = {}
    max_connections = 0

    for line in data:
        if line[0] not in connections:
            connections[line[0]] = []
        connections[line[0]].append(line[1])

        if line[1] not in connections:
            connections[line[1]] = []
        connections[line[1]].append(line[0])

    for key in connections:
        current_connections = 0
        current_password = [key]

        for value in connections[key]:
            for value2 in connections[value]:
                if value == value2:
                    continue
                else:
                    if value2 in connections[key]:
                        current_connections += 1
                        if value not in current_password:
                            current_password.append(value)
        
        if current_connections > max_connections:
            max_connections = current_connections
            password = current_password

    print(max_connections, ",".join(sorted(password)))


if __name__ == "__main__":
    data = get_data()
    #data = get_test_data()

    #part_1(data)
    part_2(data)