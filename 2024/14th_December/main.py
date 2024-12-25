import numpy as np
np.set_printoptions(threshold=np.inf)

def get_data():
    with open ("data.txt", "r") as file:
        data = file.readlines()

        # Test data
        #data = ["p=0,4 v=3,-3", "p=6,3 v=-1,-3", "p=10,3 v=-1,2", "p=2,0 v=2,-1", "p=0,0 v=1,3", "p=3,0 v=-2,-2", "p=7,6 v=-1,-3", "p=3,0 v=-1,-2", "p=9,3 v=2,3", "p=7,3 v=-1,2", "p=2,4 v=2,-3", "p=9,5 v=-3,-3"]

        data = [line.strip().split(" ") for line in data]

        positions = [[int(line[0].split(",")[0][2:]), int(line[0].split(",")[1])] for line in data]
        velocities = [[int(line[1].split(",")[0][2:]), int(line[1].split(",")[1])] for line in data]
    
    return positions, velocities


def move_robot(robot_position, robot_velocity):
    global width, height

    robot_position[0] += robot_velocity[0]
    robot_position[1] += robot_velocity[1]

    if robot_position[0] < 0:
        robot_position[0] = width + robot_position[0]
    
    if robot_position[1] < 0:
        robot_position[1] = height + robot_position[1]
    
    if robot_position[0] >= width:
        robot_position[0] = robot_position[0] - width
    
    if robot_position[1] >=  height:
        robot_position[1] = robot_position[1] - height
    
    return robot_position
    



if __name__ == "__main__":
    positions, velocities = get_data()
    width = 101
    height = 103

    iterations = 7000

    for i in range(iterations):
        for j in range(len(positions)):
            positions[j] = move_robot(positions[j], velocities[j])

        grid = np.zeros(height * width).reshape(height, width)
        
        for position in positions:
            grid[position[1]][position[0]] += 1

        if i >= 6000:
            with open("easteregg.txt", "a") as file:
                file.write(f"Iteration {i}\n")
                for row in grid:
                    file.write("".join(["#" if x > 0 else "." for x in row]) + "\n")
                file.write("\n\n")

    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0        

    for position in positions:
        if position[0] < width//2 and position[1] < height//2:
            quadrant_1 += 1
        elif position[0] > width//2 and position[1] < height//2:
            quadrant_2 += 1
        elif position[0] < width//2  and position[1] > height//2:
            quadrant_3 += 1
        elif position[0] > width//2 and position[1] > height//2:
            quadrant_4 += 1

    safety_factor = quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4

    print(safety_factor)


