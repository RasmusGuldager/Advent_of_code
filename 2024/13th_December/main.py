def get_data():
    with open("data.txt", "r") as file:
        data = file.readlines()
        data = [x.strip() for x in data]

        # Test data
        #data = ["Button A: X+94, Y+34", "Button B: X+22, Y+67", "Prize: X=8400, Y=5400", "", "Button A: X+26, Y+66", "Button B: X+67, Y+21", "Prize: X=12748, Y=12176", "", "Button A: X+17, Y+86", "Button B: X+84, Y+37", "Prize: X=7870, Y=6450", "", "Button A: X+69, Y+23", "Button B: X+27, Y+71", "Prize: X=18641, Y=10279"]

        buttons_a = []
        buttons_b = []
        prizes = []

        for i in range(len(data)):
            if i % 4 == 0:
                buttons_a.append(data[i].split(": ")[1])
            elif i % 4 == 1:
                buttons_b.append(data[i].split(": ")[1])
            elif i % 4 == 2:
                prizes.append(data[i].split(": ")[1])
        
        for i in range(len(buttons_a)):
            buttons_a[i] = buttons_a[i].split(", ")
            buttons_a[i][0] = int(buttons_a[i][0][2:])
            buttons_a[i][1] = int(buttons_a[i][1][2:])

            buttons_b[i] = buttons_b[i].split(", ")
            buttons_b[i][0] = int(buttons_b[i][0][2:])
            buttons_b[i][1] = int(buttons_b[i][1][2:])

            prizes[i] = prizes[i].split(", ")
            prizes[i][0] = int(prizes[i][0][2:]) + 10000000000000
            prizes[i][1] = int(prizes[i][1][2:]) + 10000000000000

            
    return buttons_a, buttons_b, prizes

def find_price(button_a, button_b, prize):
    offset_a = 0
    offset_b = 1
    while True:
        if offset_b > 100:
            offset_a += 1
            offset_b = 0
        
        if offset_a > 100:
            return False

        if prize[0] == button_a[0] * offset_a + button_b[0] * offset_b and prize[1] == button_a[1] * offset_a + button_b[1] * offset_b:
            print(offset_a, offset_b)
            return offset_a * 3 + offset_b
        
        offset_b += 1


def part_1():
    buttons_a, buttons_b, prizes = get_data()
    price = 0
    for i in range(len(buttons_a)):
        price += find_price(buttons_a[i], buttons_b[i], prizes[i])

    print(price)


def find_price_part_2(button_a, button_b, prize):
    offset_b = prize[1] // button_b[1]

    while True:
        print(offset_b)
        if prize[0] - button_b[0] * offset_b % button_a[0] == 0:
            offset_a = (prize[0] - button_b[0] * offset_b) // button_a[0]
            print("Done")
            return offset_a * 3 + offset_b
        else:
            offset_b -= 1
        
        if offset_b < 0:
            print("Done")
            return False

        
def part_2():
    buttons_a, buttons_b, prizes = get_data()
    price = 0
    for i in range(len(buttons_a)):
        price += find_price_part_2(buttons_a[i], buttons_b[i], prizes[i])

    print(price)


if __name__ == "__main__":
    #part_1()

    part_2()