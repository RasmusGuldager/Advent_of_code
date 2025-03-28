

def get_data(test=False):
    seeds: list = []
    seed_to_soil: list = []
    soil_to_fert: list = []
    fert_to_water: list = []
    water_to_light: list = []
    light_to_temp: list = []
    temp_to_hum: list = []
    hum_to_loc: list = []

    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()

        seeds = [int(num) for num in data[1].strip().split(" ")]
        seed_to_soil = [[int(num) for num in line.strip().split(" ")] for line in data[4:13]]
        soil_to_fert = [[int(num) for num in line.strip().split(" ")] for line in data[15:58]]
        fert_to_water = [[int(num) for num in line.strip().split(" ")] for line in data[60:106]]
        water_to_light = [[int(num) for num in line.strip().split(" ")] for line in data[108:148]]
        light_to_temp = [[int(num) for num in line.strip().split(" ")] for line in data[150:187]]
        temp_to_hum = [[int(num) for num in line.strip().split(" ")] for line in data[189:207]]
        hum_to_loc = [[int(num) for num in line.strip().split(" ")] for line in data[209:251]]

    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()
  
        seeds = [int(num) for num in data[1].strip().split(" ")]
        seed_to_soil = [[int(num) for num in line.strip().split(" ")] for line in data[4:6]]
        soil_to_fert = [[int(num) for num in line.strip().split(" ")] for line in data[8:11]]
        fert_to_water = [[int(num) for num in line.strip().split(" ")] for line in data[13:17]]
        water_to_light = [[int(num) for num in line.strip().split(" ")] for line in data[19:21]]
        light_to_temp = [[int(num) for num in line.strip().split(" ")] for line in data[23:26]]
        temp_to_hum = [[int(num) for num in line.strip().split(" ")] for line in data[28:30]]
        hum_to_loc = [[int(num) for num in line.strip().split(" ")] for line in data[32:34]]
    
    return seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc
    


def part_1(seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc):
    possible_locations: list = []

    for seed in seeds:
        soil_number = None
        for soil in seed_to_soil:
            if soil[1] <= seed < soil[1] + soil[2]:
                soil_number = soil[0] + seed - soil[1]
                break 
        if soil_number is None:
            soil_number = seed
        
        fert_number = None
        for fert in soil_to_fert:
            if fert[1] <= soil_number < fert[1] + fert[2]:
                fert_number = fert[0] + soil_number - fert[1]
                break
        if fert_number is None:
            fert_number = soil_number

        water_number = None
        for water in fert_to_water:
            if water[1] <= fert_number < water[1] + water[2]:
                water_number = water[0] + fert_number - water[1]
                break
        if water_number is None:
            water_number = fert_number

        light_number = None
        for light in water_to_light:
            if light[1] <= water_number < light[1] + light[2]:
                light_number = light[0] + water_number - light[1]
                break
        if light_number is None:
            light_number = water_number
        
        temp_number = None
        for temp in light_to_temp:
            if temp[1] <= light_number < temp[1] + temp[2]:
                temp_number = temp[0] + light_number - temp[1]
                break
        if temp_number is None:
            temp_number = light_number
        
        hum_number = None
        for hum in temp_to_hum:
            if hum[1] <= temp_number < hum[1] + hum[2]:
                hum_number = hum[0] + temp_number - hum[1]
                break
        if hum_number is None:
            hum_number = temp_number

        loc_number = None
        for loc in hum_to_loc:
            if loc[1] <= hum_number < loc[1] + loc[2]:
                loc_number = loc[0] + hum_number - loc[1]
                break
        if loc_number is None:
            loc_number = hum_number
        
        possible_locations.append(loc_number)

    
    print(min(possible_locations))



if __name__ == "__main__":
    seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc = get_data()
    
    part_1(seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc)

