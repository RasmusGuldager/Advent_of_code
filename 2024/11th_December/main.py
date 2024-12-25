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



def blink_part_2(data):
    return_data = {}
    for key in data:
        if key == 0:
            if 1 not in return_data:
                return_data[1] = data[key]
            else:
                return_data[1] += data[key]

        elif len(str(key)) % 2 == 0:
            part_1 = int(str(key)[:len(str(key)) // 2])
            part_2 = int(str(key)[len(str(key)) // 2:])
            if part_1 not in return_data:
                return_data[part_1] = data[key]
            else:
                return_data[part_1] += data[key]

            if part_2 not in return_data:
                return_data[part_2] = data[key]
            else:
                return_data[part_2] += data[key]
        
        else:
            if key * 2024 not in return_data:
                return_data[key * 2024] = data[key]
            else:
                return_data[key * 2024] += data[key]
    return return_data


def main(iterations, data):
    for i in range(iterations): 
       print(i*100/iterations) 
       #data = blink(data)
       data = blink_part_2(data)
    
    return data



if __name__ == "__main__":
    #data = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]
    data = {0: 1, 7: 1, 6618216: 1, 26481: 1, 885: 1, 42: 1, 202642: 1, 8791: 1}
    iterations = 75


    # Test data
    #data = {17: 1, 125: 1}
    #iterations = 6

    data = main(iterations, data)
    print(len(data)) # Answer is 213625

    # Part 2
    part_2_answer = 0
    for key in data:
        part_2_answer += data[key]

    print(part_2_answer) # Answer is 213625
