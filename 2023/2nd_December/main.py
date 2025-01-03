def get_data():
    with open("data.txt") as file:
        games = file.readlines()
        games = [game.strip() for game in games]

        sets = [[] for _ in range(len(games))]

        for index, game in enumerate(games):
            set = game[game.index(":") + 2:]
            set = set.split("; ")
            for _ in range(len(set)):
                sets[index].append({})
            for ind, s in enumerate(set):
                s = s.split(", ")
                for i in range(len(s)):
                    s[i] = s[i].split(" ")
                    sets[index][ind][s[i][1]] = int(s[i][0])

        return sets

            
def main(data):
    rules = {"red": 12, "green": 13, "blue": 14}

    answer = 0

    for index, game in enumerate(data):
        possible = True
        for i, set in enumerate(game):
            for key, value in set.items():
                if value > rules[key]:
                    possible = False
                    break
        
            if possible and i == len(game) - 1:
                answer += index + 1

            elif i == len(game) - 1:
                possible = True

    print(answer)

    power = 0

    for game in data:
        rules = {"red": 0, "green": 0, "blue": 0}
        for set in game:
            for key, value in set.items():
                if value > rules[key]:
                    rules[key] = value
        power += rules["red"] * rules["green"] * rules["blue"]

    print(power)
                    

if __name__ == "__main__":
    data = get_data()
    main(data)
                