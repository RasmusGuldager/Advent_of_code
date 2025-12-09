import re

def get_data(test=False):
	if not test:
		with open("data.txt", "r") as file:
			data = file.readlines()
	else:
		with open("test_data.txt", "r") as file:
			data = file.readlines()

	data = [re.split(r'\s+', line.strip()) for line in data]

	numbers = data[:-1]
	operations = data[-1]

	return numbers, operations


def part_1(numbers, operations):
	total = 0

	for i, operation in enumerate(operations):
		if operation == "+":
			answer = 0
		else:
			answer = 1

		for row in numbers:
			if operation == "+":
				answer += int(row[i])
			else:
				answer *= int(row[i])
		
		total += answer

	print("Part 1:", total)


if __name__ == '__main__':
	numbers, operations = get_data()

	part_1(numbers, operations)