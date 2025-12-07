def get_data(test=False):
	if not test:
		with open("data.txt", "r") as file:
			data = file.readlines()
	else:
		with open("test_data.txt", "r") as file:
			data = file.readlines()

	ranges = []
	ingredients = []

	for line in data:
		if "-" in line:
			ranges.append([int(x) for x in line.strip().split("-")])
		else:
			ingredients.append(int(line.strip()))

	return ranges, ingredients


def part_1(ranges, ingredients):
	good_ingredients = 0

	for ingredient in ingredients:
		for range in ranges:
			if range[0] <= ingredient <= range[1]:
				good_ingredients += 1
				break
	
	print("Part 1:", good_ingredients)


if __name__ == '__main__':
	ranges, ingredients = get_data()

	part_1(ranges, ingredients)