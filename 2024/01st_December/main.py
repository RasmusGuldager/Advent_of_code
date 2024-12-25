import numpy as np

with open("data.txt", "r") as file:
    data_right  = np.zeros(1000)
    data_left = np.zeros(1000)
    index = 0

    for line in file:
        data = line.split()
        data_right[index] = data[1]
        data_left[index] = data[0]
        index += 1    

# test data
# data_right = np.array([4, 3, 5, 3, 9, 3])
# data_left = np.array([3, 4, 2, 1, 3, 3])        
    
data_right.sort()
data_left.sort()

distance = 0

for i in range(len(data_right)):
    distance += abs(data_right[i] - data_left[i])

#print(distance) # answer is 936063

similarity_score = 0

for i in range(len(data_right)):
    if data_left[i] in data_right:
        occurrences = np.count_nonzero(data_right == data_left[i])
        similarity_score += data_left[i] * occurrences

#print(similarity_score) # answer is 23150395 