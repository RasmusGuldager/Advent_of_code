def get_data(test=False):
    with open("data.txt") as file:

        data = file.readlines()

    if not test:
        times = [int(x) for x in data[0].strip().split(",")]
        dists = [int(x) for x in data[1].strip().split(",")]

    else:
        times = [int(x) for x in data[3].strip().split(",")]
        dists = [int(x) for x in data[4].strip().split(",")]

    return times, dists


def part_1(times, dists):
    different_ways_to_win = []

    for index, time in enumerate(times):
        beats_record = 0

        for i in range(time):
            if (time - i) * i > dists[index]:
                beats_record += 1
            elif beats_record > 0:
                break

        different_ways_to_win.append(beats_record)

    ans = 1
    for i in different_ways_to_win:
        ans *= i

    print(f"Part 1: {ans}")


def part_2(times, dists):
    time = [str(x) for x in times]
    time = int("".join(time))

    dist = [str(x) for x in dists]
    dist = int("".join(dist))

    min = 0
    max = 0

    for i in range(time):
        if (time - i) * i > dist:
            min = i
            break

    for i in range(time, 0, -1):
        if (time - i) * i > dist:
            max = i+1
            break
    
    print(f"Part 2: {max-min}")


if __name__ == "__main__":
    times, dists = get_data()

    part_1(times, dists)
    part_2(times, dists)
