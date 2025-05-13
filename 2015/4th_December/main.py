import hashlib

def get_data(test=False):
	with open('data.txt', 'r') as file:
		data = file.read()
		
	return data


if __name__ == '__main__':
	input = get_data()
	
	number = 0

	while True:
		key = input + str(number)
		result = hashlib.md5(key.encode()).hexdigest()
		
		if result.startswith("000000"):
			print(number)
			break

		number += 1

