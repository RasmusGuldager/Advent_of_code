

def is_valid_index(index, length):
    return 0 <= index < length

def safe_substring(line, start, end):
    if start < 0 or end < 0 or start >= len(line) or end > len(line):
        return None
    return line[start:end]


with open("data.txt", "r") as file:
    data = file.readlines()

    pattern = "MAS"
    rev_pattern = "SAM"

    XMAS_count = 0

    # test data
    #data = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

    line_length = len(data[0])
    data_length = len(data)

    for line_index, line in enumerate(data):
        for letter_index, letter in enumerate(line):
            if letter == "X":

                # Check horizontal
                if is_valid_index(letter_index + 3, line_length):
                    if safe_substring(line, letter_index + 1, letter_index + 4) == pattern:
                        #print(f"Found pattern 1 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check reverse horizontal
                if is_valid_index(letter_index - 3, line_length):
                    if safe_substring(line, letter_index - 3, letter_index) == rev_pattern:
                        #print(f"Found pattern 2 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check vertical
                if is_valid_index(line_index + 3, data_length):
                    if data[line_index + 1][letter_index] + data[line_index + 2][letter_index] + data[line_index + 3][letter_index] == pattern:
                        #print(f"Found pattern 3 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check reverse vertical
                if is_valid_index(line_index - 3, data_length):
                    if data[line_index - 3][letter_index] + data[line_index - 2][letter_index] + data[line_index - 1][letter_index] == rev_pattern:
                        #print(f"Found pattern 4 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check diagonal up-right
                if is_valid_index(line_index - 3, data_length) and is_valid_index(letter_index + 3, line_length):
                    if data[line_index - 1][letter_index + 1] + data[line_index - 2][letter_index + 2] + data[line_index - 3][letter_index + 3] == pattern:
                        #print(f"Found pattern 5 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check diagonal up-left
                if is_valid_index(line_index - 3, data_length) and is_valid_index(letter_index - 3, line_length):
                    if data[line_index - 1][letter_index - 1] + data[line_index - 2][letter_index - 2] + data[line_index - 3][letter_index - 3] == pattern:
                        #print(f"Found pattern 6 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check diagonal down-right
                if is_valid_index(line_index + 3, data_length) and is_valid_index(letter_index + 3, line_length):
                    if data[line_index + 1][letter_index + 1] + data[line_index + 2][letter_index + 2] + data[line_index + 3][letter_index + 3] == pattern:
                        #print(f"Found pattern 7 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1

                # Check diagonal down-left
                if is_valid_index(line_index + 3, data_length) and is_valid_index(letter_index - 3, line_length):
                    if data[line_index + 1][letter_index - 1] + data[line_index + 2][letter_index - 2] + data[line_index + 3][letter_index - 3] == pattern:
                        #print(f"Found pattern 8 at index {letter_index} in line: {line_index}")
                        XMAS_count += 1
                    
    print(f"Total count of XMAS pattern is: {XMAS_count}") # Answer is 2532


    # Part 2

    x_MAS_count = 0

    for line_index, line in enumerate(data):
        for letter_index, letter in enumerate(line):
            if letter == "A":
                if is_valid_index(letter_index-1, line_length) and is_valid_index(letter_index+1, line_length) and is_valid_index(line_index-1, data_length) and is_valid_index(line_index+1, data_length):
                    diagonal_one = {"M": 0, "S": 0}
                    diagonal_two = {"M": 0, "S": 0}

                    try:
                        diagonal_one[data[line_index + 1][letter_index + 1]] += 1
                        diagonal_one[data[line_index - 1][letter_index - 1]] += 1
                        diagonal_two[data[line_index - 1][letter_index + 1]] += 1
                        diagonal_two[data[line_index + 1][letter_index - 1]] += 1

                    except KeyError:
                        continue

                    if diagonal_one["M"] == 1 and diagonal_one["S"] == 1 and diagonal_two["M"] == 1 and diagonal_two["S"] == 1:
                        print(f"Found pattern at index {letter_index} in line: {line_index}")
                        x_MAS_count += 1

    print(f"Total count of x MAS patterns is: {x_MAS_count}") # Answer is 1941
