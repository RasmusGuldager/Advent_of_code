def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    if test:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    patterns: list[str] = []

    pattern = []
    for line in data:
        line = line.strip()
        if not line == "":
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

    return patterns


def part_1(patterns):
    note_summary = 0

    for pattern in patterns:
        vert_mirrors = [i for i in range(1, len(pattern[0]))]
        hori_mirrors = [i for i in range(1, len(pattern))]

        # Check for vertical mirror
        for i in range(1, len(pattern[0])):
            for line in pattern:
                left_index = i - 1
                right_index = i

                while left_index >= 0 and right_index < len(line):
                    if line[left_index] != line[right_index]:
                        if i in vert_mirrors:
                            vert_mirrors.remove(i)
                        break
                    else:
                        left_index -= 1
                        right_index += 1

        # Check for horizontal mirror
        for i in range(1, len(pattern)):
            for j in range(len(pattern[0])):
                left_index = i - 1
                right_index = i

                while left_index >= 0 and right_index < len(pattern):
                    if pattern[left_index][j] != pattern[right_index][j]:
                        if i in hori_mirrors:
                            hori_mirrors.remove(i)
                        break
                    else:
                        left_index -= 1
                        right_index += 1

        if len(vert_mirrors) > 0:
            note_summary += vert_mirrors[0]
        else:
            note_summary += hori_mirrors[0] * 100

    print(f"Part 1: {note_summary}")


if __name__ == "__main__":
    patterns = get_data()

    part_1(patterns)
