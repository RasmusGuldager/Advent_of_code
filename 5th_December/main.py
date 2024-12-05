import numpy as np

def check_truthfullness(update):
    test_results = 0
    for page_number in update:
        if len(page_number_indicies_left[int(page_number)]) == 0:
            test_results += 1
            
        for j, index in enumerate(page_number_indicies_left[int(page_number)]):
            try:
                if update.index(int(page_number)) < update.index(int(rules_right[index])):
                    pass
                else:
                    break

            except IndexError:
                pass

            except ValueError:
                pass 
   
            if j == len(page_number_indicies_left[int(page_number)]) - 1:
                test_results += 1
            
    if test_results == len(update):
        return True
        
    return False


def fix_update(update):
    for page_number in update:
        for index in page_number_indicies_left[int(page_number)]:
            try:
                if update.index(int(page_number)) < update.index(int(rules_right[index])):
                    pass
                else:
                    update[update.index(int(page_number))], update[update.index(int(rules_right[index]))] = update[update.index(int(rules_right[index]))], update[update.index(int(page_number))]

            except IndexError:
                pass

            except ValueError:
                   pass 
        
    return update


with open("data.txt", "r") as file:
    data = data = [line.strip() for line in file.readlines()]

    rules_right = np.zeros(1176)
    rules_left = np.zeros(1176)

    updates = []

    sum_of_middle_page_numbers = 0

    # Parse rules
    for i in range(1176):
        rules_right[i] = data[i].split("|")[1]
        rules_left[i] = data[i].split("|")[0]

    # Testdata: rules
    #rules_right = [53, 13, 61, 47, 29, 13, 53, 13, 29, 29, 53, 53, 29, 13, 47, 75, 61, 61, 29, 13, 13]
    #rules_left = [47, 97, 97, 97, 75, 61, 75, 29, 97, 53, 61, 97, 61, 47, 75, 97, 47, 75, 47, 75, 53]

    # Find page number range
    page_number_min = int(min(min(rules_left), min(rules_right)))
    page_number_max = int(max(max(rules_left), max(rules_right)))

    # Create dictionary for page number indicies
    page_number_indicies_right = {i: [] for i in range(page_number_min, page_number_max + 1)}
    page_number_indicies_left = {i: [] for i in range(page_number_min, page_number_max + 1)}

    # Fill dictionary with indicies
    for i in range(len(rules_right)):
        page_number_indicies_right[rules_right[i]].append(i)
        page_number_indicies_left[rules_left[i]].append(i)

    # Parse updates
    for i in range(194):
        updates.append(data[i + 1177].split(","))
        for j in range(len(updates[i])):
            updates[i][j] = int(updates[i][j])


    # Testdata: updates
    #updates = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]

    ordered_updates_indicies = []

    for i, update in enumerate(updates):
        # Check all rules for specific page number
        test_results = 0
        if check_truthfullness(update):
            sum_of_middle_page_numbers += int(update[len(update) // 2])
            ordered_updates_indicies.append(i)
    
    print(sum_of_middle_page_numbers) # Answer is 6051

    sum_of_middle_page_numbers_part_2 = 0


    # Part 2

    for i, update in enumerate(updates):
        if i not in ordered_updates_indicies:
            fixed_update = fix_update(update)

            while not check_truthfullness(fixed_update):
                fixed_update = fix_update(fixed_update)
            
            #print(update, check_truthfullness(update))
            sum_of_middle_page_numbers_part_2 += int(update[len(update) // 2])


    print(sum_of_middle_page_numbers_part_2) # Answer is lower than 5353
