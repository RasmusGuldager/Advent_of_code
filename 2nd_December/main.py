

with open("data.txt", "r") as file:
    levels = [[] for i in range(1000)]
    iteration = 0

    for line in file:
        levels[iteration] = [int(i) for i in line.split()]
        iteration += 1


# test data
#levels = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

safe_reports = 0
safe_indices = []

def is_safe(level, j):
    if level == sorted(level):
        for i in range(1, len(level)):
            if (1 <= (level[i] - level[i-1])) and ((level[i] - level[i-1]) <= 3):
                pass
            else:
                return False

            if i == len(level) - 1:
                safe_indices.append(j)  
                return True

    elif level == sorted(level, reverse=True):
        for i in range(1, len(level)):
            if (1 <= (level[i-1] - level[i])) and ((level[i-1] - level[i]) <= 3):
                pass
            else:
                return False

            if i == len(level) - 1:
                safe_indices.append(j)  
                return True
    
    else:
        return False
                


for i in range(len(levels)):
    safe_reports += is_safe(levels[i], i)

#print(safe_reports) # Answer is 224


# Part 2

for i in range(len(levels)):
    if i not in safe_indices:
        for j in range(len(levels[i])):
            temp_level = levels[i][:j] + levels[i][j+1:]
            safe_reports += is_safe(temp_level, i)
            if is_safe(temp_level, i):
                break


print(safe_reports) # Answer is 293
    