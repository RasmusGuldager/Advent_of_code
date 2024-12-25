
def try_combinations(answer, numbers):
    # Try all combinations of multiplying and adding the numbers
    for i in range(2**len(numbers)):
        total = 0
        for j in range(len(numbers)):
            if i & 2**j:
                total += numbers[j]
            else:
                total *= numbers[j]
        if total == answer:
            return True
    return False

def try_combinations_with_concatenation(answer, numbers):
    pass
    


with open("data.txt", "r") as file:
    data = file.readlines()
    
    data = [line.strip() for line in data]
    data = [line.split(":") for line in data]

    answers = [int(line[0]) for line in data]

    numbers = [[int(num) for num in line[1].split()] for line in data]

    # Test data
    #answers = [190, 3267, 83, 156, 7290, 161011, 192, 21037, 292]
    #numbers = [[10, 19], [81, 40, 27], [17, 5], [15, 6], [6, 8, 6, 15], [16, 10, 13], [17, 8, 14], [9, 7, 18, 13], [11, 6, 16, 20]]


    total_calibration = 0

    for i in range(len(answers)):
        min_value = sum(numbers[i])
        max_value = 1
        for j in range(len(numbers[i])): 
            max_value *= numbers[i][j]

        if min_value > answers[i] > max_value:
            continue
        elif min_value == answers[i] or answers[i] == max_value:
            total_calibration += answers[i]

        else:
            if try_combinations(answers[i], numbers[i]):
                total_calibration += answers[i]
    
    
    #print(total_calibration) # Answer is 5702958180383

    # Part 2

    total_calibration_part_2 = 0

    for i in range(len(answers)):
        if try_combinations(answers[i], numbers[i]):
            total_calibration_part_2 += answers[i]
        else:
            pass