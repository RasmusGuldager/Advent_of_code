with open("cleaned_data_pt1.txt", "r") as file:
    data = file.readlines()

    answer = 0
    mul = lambda x, y: x * y

    for line in data:
        answer += eval(line)
    
    #print(answer) # Answer is 167650499
    
with open("cleaned_data_pt2.txt", "r") as file:
    data = file.readlines()

    answer = 0

    mul = lambda x, y: x * y

    instruction = 1

    for line in data:
        if "don't" in line:
            instruction = 0
            continue
        elif "do" in line:
            instruction = 1
        elif "mul" in line and instruction == 1:
            answer += eval(line)
    
    print(answer)
            
