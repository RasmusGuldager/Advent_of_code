def blink(data):
    offset = 0
    for i in range(len(data)):
        if data[i + offset] == 0:
            data[i + offset] = 1

        elif len(str(data[i + offset])) % 2 == 0:
            num = data.pop(i + offset)
            data.insert(i + offset, int(str(num)[:len(str(num)) // 2]))
            data.insert(i + offset + 1, int(str(num)[len(str(num)) // 2:]))
            offset += 1
        else:
            data[i + offset] *= 2024

    return data


def main(iterations, data):
    for i in range(iterations): 
       print(i*100/iterations) 
       data = blink(data)



if __name__ == "__main__":
    data = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]
    iterations = 25

    # Test data
    #data = [125, 17]
    #iterations = 6

    main(iterations, data)
    print(len(data)) # Answer is 213625

