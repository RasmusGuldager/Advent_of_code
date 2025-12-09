def get_data(test=False):
	with open('data.txt', 'r') as file:
		data = file.read().split(",")

	return data


def part_1(data):
	result: int = 0

	for string in data:
		value: int = 0
		for letter in string:
			value += ord(letter)
			value *= 17
			value %= 256
		
		result += value
	
	print(result)
			


if __name__ == '__main__':
	data = get_data()

	part_1(data)