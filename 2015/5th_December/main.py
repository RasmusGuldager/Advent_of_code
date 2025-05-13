def get_data(test=False):
    with open("data.txt", "r") as file:
        data = file.readlines()

    data = [line.strip() for line in data]
    return data


def part_1(data):
    bad_strings = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]
    good_strings: int = 0

    for line in data:
        good_string: bool = True

        for string in bad_strings:
            if string in line:
                good_string = False
                break

        vowel_count: int = 0
        for vowel in vowels:
            vowel_count += line.count(vowel)

        if vowel_count < 3:
            good_string = False

        last_letter = line[0]
        double_letter = False
        for letter in line[1:]:
            if letter == last_letter:
                double_letter = True
            else:
                last_letter = letter

        if not double_letter:
            good_string = False

        good_strings += good_string

    print(good_strings)
    

def part_2(data):
	good_strings: int = 0
    
	for line in data[-1:]:
		good_string = True
          
		for index in range(1, len(line)):
			combo = line[index-1:index+1]
               


if __name__ == "__main__":
    data = get_data()

    part_1(data)
    part_2(data)
