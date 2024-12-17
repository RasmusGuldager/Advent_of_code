def get_combo_operand(operand, register_a, register_b, register_c):
    match operand:
        case 4:
            return register_a
        
        case 5:
            return register_b
        
        case 6:
            return register_c
        
        case 7:
            raise Exception("Invalid instruction")
        
        case _ :
            return operand


def clock_cycle(instruction, operand, register_a, register_b, register_c, instruction_pointer):
    match instruction:
        case 0:
            #print(register_a, get_combo_operand(operand, register_a, register_b, register_c), register_a / (get_combo_operand(operand, register_a, register_b, register_c) ** 2))
            register_a = register_a // (2 ** get_combo_operand(operand, register_a, register_b, register_c))

        case 1:
            register_b = operand ^ register_b
        
        case 2:
            register_b = get_combo_operand(operand, register_a, register_b, register_c) % 8
        
        case 3:
            if register_a == 0:
                pass
            else:
                instruction_pointer = operand
                return register_a, register_b, register_c, instruction_pointer
        
        case 4:
            register_b = register_b ^ register_c
        
        case 5:
            output.append(get_combo_operand(operand, register_a, register_b, register_c) % 8)
        
        case 6:
            register_b = register_a // (2 ** get_combo_operand(operand, register_a, register_b, register_c))
        
        case 7:
            register_c = register_a // (2 ** get_combo_operand(operand, register_a, register_b, register_c))

    
    return register_a, register_b, register_c, instruction_pointer + 2


if __name__ == "__main__":
    register_a = 218330300000000
    register_b = 0
    register_c = 0

    program = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]

    # Test data
    #register_a = 117440
    #register_b = 0
    #register_c = 0

    #program = [0,3,5,4,3,0]

    output = []
    instruction_pointer = 0

    while instruction_pointer < len(program):
        register_a, register_b, register_c, instruction_pointer = clock_cycle(program[instruction_pointer], program[instruction_pointer + 1], register_a, register_b, register_c, instruction_pointer)
        
    print((",").join([str(x) for x in output]))
    
    counter = 236580000000000

    while True:
        while instruction_pointer < len(program):
            register_a, register_b, register_c, instruction_pointer = clock_cycle(program[instruction_pointer], program[instruction_pointer + 1], register_a, register_b, register_c, instruction_pointer)
        
        if output == program:
            print(register_a)
            break
        else:
            if counter % 10000000000 == 0:
                print(counter, output, len(output))

            output = []
            instruction_pointer = 0
            counter += 100000000
            register_a = counter

#    program = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]
