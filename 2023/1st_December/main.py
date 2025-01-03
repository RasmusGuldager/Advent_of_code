import re

def get_data():
    with open("data.txt") as file:
        data = file.readlines()
        data = [line.strip() for line in data]

    return data

def get_test_data():
    data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    
    return data

def main(data):
    answer = 0
    numbers = "0123456789"
    word_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in data:
        digits = []
        letters = ""
        for letter in line:
            if letter in numbers:
                digits.append(letter)
                letters = ""
            else:
                letters += letter
                for i, word in enumerate(word_numbers):
                    if word in letters:
                        digits.append(str(i))
                        letters = f"{word[-1]}"
        
        if len(digits) > 0:
            answer += int(digits[0] + digits[-1])

    print(answer)



if __name__ == "__main__":
    data = get_data()
    #data = get_test_data()

    main(data)