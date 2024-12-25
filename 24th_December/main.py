def get_data(test=False):

    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
            data = [line.strip() for line in data]
    else:
        with open("testdata.txt", "r") as file:
            data = file.readlines()
            data = [line.strip() for line in data]

    registers = {}
    operations = []

    for line in data:
        split_line = line.split(" ")
        if len(split_line) == 2:
            registers[split_line[0][:-1]] = int(split_line[1])
        
        elif len(split_line) == 5:
            operations.append([split_line[0], split_line[1], split_line[2], split_line[4]])
    

    return registers, operations

def and_op(value1, value2):
    print("and", value1, value2, value1 & value2)
    return value1 & value2
    

def or_op(value1, value2):
    print("or", value1, value2, value1 | value2)
    return value1 | value2


def xor_op(value1, value2):
    print("xor", value1, value2, value1 ^ value2)
    return value1 ^ value2


def main(registers, operations):
    while len(operations) > 0:  
        operation = operations.pop(0)
        try:
            if operation[1] == "AND":
                registers[operation[3]] = and_op(registers[operation[0]], registers[operation[2]])
                
            elif operation[1] == "OR":
                registers[operation[3]] = or_op(registers[operation[0]], registers[operation[2]])

            elif operation[1] == "XOR":
                registers[operation[3]] = xor_op(registers[operation[0]], registers[operation[2]])
        except KeyError:
            operations.append(operation)

    answers = []

    for key in registers:
        if key[0] == "z":
            answers.append([key, registers[key]])
    
    answers.sort(reverse=True)
    answer = []

    for i in range(len(answers)):
        answer.append(str(answers[i][1]))

    answer = "".join(answer)

    print(answer)


if __name__ == "__main__":
    registers, operations = get_data(test = False)
    
    main(registers, operations)
    