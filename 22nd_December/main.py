def get_data():
    with open("data.txt", "r") as file:
        data = file.readlines()
        data = [int(i) for i in data]
        
    return data

def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216


def generate_next_number(number):
    number = prune(mix(number, number * 64))
    number = prune(mix(number, number // 32))
    number = prune(mix(number, number * 2048))

    return number


def generate_sequences():
    sequences = []
    for d1 in range(-9, 10):
        for d2 in range(-9, 10):
            for d3 in range(-9, 10):
                for d4 in range(-9, 10):
                    if abs(d1 - d2) > 10 or abs(d2 - d3) > 10 or abs(d3 - d4) > 10:
                        continue
                    elif d1 + d2 + d3 + d4 > 20 or d1 + d2 + d3 + d4 < -20:
                        continue
                    else:
                        sequences.append([d1, d2, d3, d4])
    return sequences        



if __name__ == "__main__":
    data = get_data()
    answer = 0

    sequences = generate_sequences()


    prices = [int(str(data[0])[-1])]
    price_changes = []

    for i in range(len(data)):
        number = data[i]
        for j in range(2000):
            number = generate_next_number(number)
        answer += number

    print(answer, prices)
    print(len(sequences))
    