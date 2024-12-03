import re

# Part 1

#with open("uncleaned_data.txt", "r") as file:
#   data = file.read()
#
#    pattern = r"mul\(\d+,\d+\)"
#
#    matches = re.findall(pattern, data)


# Part 2

with open("uncleaned_data.txt", "r") as file:
    data = file.read()

    pattern = r"(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don't\(\))"

    matches = re.findall(pattern, data)



with open("cleaned_data_pt2.txt", "w") as file:
    for match in matches:    
        file.write(match + "\n")