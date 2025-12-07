def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.read().strip().split(",")
    else:
        with open("test_data.txt", "r") as file:
            data = file.read().strip().split(",")

    data = [list(map(int, line.split("-"))) for line in data]
    
    return data


def part_1(data):
    invalid = 0

    for id_range in data:
        min = id_range[0]
        max = id_range[1]

        for i in range(min, max+1):
            temp = str(i)
            length = len(temp) // 2
            left = temp[0:length]
            right = temp[length:]

            if left == right:
                invalid += i

    print("Part 1:", invalid)


def part_2(data):
    invalid = set()

    for id_range in data:
        min = id_range[0]
        max = id_range[1]
        
        for i in range(min, max+1):
            length = len(str(i))

            # Calculate possible pattern lengths
            pattern_lengths = []
            for j in range(1,length):
                if length % j == 0:
                    pattern_lengths.append(j)

            temp = str(i)

            candidate_patterns = []
            for pattern_length in pattern_lengths:
                candidate_patterns.append(temp[:pattern_length])
            
            for candidate_pattern in candidate_patterns:
                if candidate_pattern*(length // len(candidate_pattern)) == temp:
                    invalid.add(i)
    
    print("Part 2:", sum(invalid))



if __name__ == "__main__":
    data = get_data()

    part_1(data)
    part_2(data)
