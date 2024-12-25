def check_position(guard_position):
    return 0 < guard_position[0] < len(data[0]) + 1 and 0 < guard_position[1] < len(data) + 1


def move_guard(guard, direction):
    if direction == "up":
        guard[1] -= 1
    elif direction == "right":
        guard[0] += 1
    elif direction == "down":
        guard[1] += 1
    elif direction == "left":
        guard[0] -= 1

def check_obstacle(guard_position):
    if guard_direction == "up":
        if data[guard_position[1] - 1][guard_position[0]] == "#":
            return True
    elif guard_direction == "right":
        if data[guard_position[1]][guard_position[0] + 1] == "#":
            return True
    elif guard_direction == "down":
        if data[guard_position[1] + 1][guard_position[0]] == "#":
            return True
    elif guard_direction == "left":
        if data[guard_position[1]][guard_position[0] - 1] == "#":
            return True

    return False        


with open("data.txt", "r") as file:
    data = file.readlines()

    data = [line.strip() for line in data]

    guard_directions = ["up", "right", "down", "left"]
    guard_direction = "up"

    # x, y: Column, line
    guard_position = [85, 65]

    # Test guard position
    #guard_position = [4, 6]

    # Test data
    #data = ["....#.....", ".........#", "..........", "..#.......", ".......#..", "..........", ".#..^.....", "........#.", "#.........", "......#..."]

    visited_indices = [[guard_position[0], guard_position[1]]]
    visited_places_count = 1

    while check_position(guard_position):
        obstacle = check_obstacle(guard_position)
        if not obstacle:
            move_guard(guard_position, guard_direction)
            if guard_position not in visited_indices:
                visited_indices.append(guard_position.copy())
                visited_places_count += 1
    
        else:
            guard_direction = guard_directions[(guard_directions.index(guard_direction) + 1) % 4]
            continue


    
    print(visited_places_count) # Answer is 5030


    # Part 2

    while check_position(guard_position):
        obstacle = check_obstacle(guard_position)
        if not obstacle:
            move_guard(guard_position, guard_direction)
            if guard_position not in visited_indices:
                visited_indices.append(guard_position.copy())
                visited_places_count += 1
    
        else:
            guard_direction = guard_directions[(guard_directions.index(guard_direction) + 1) % 4]
            continue
