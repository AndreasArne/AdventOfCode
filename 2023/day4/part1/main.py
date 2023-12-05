with open("data.txt") as fd:
    data = fd.read()
data = data.replace("  ", " ")
data = data.splitlines()

points = 0
for whole_line in data:
    JUMP_PAST_SPACE = 2
    start_index = whole_line.index(":")
    all_numbers = whole_line[start_index+JUMP_PAST_SPACE:].split(" | ")
    winning_nrs = all_numbers[0].split(" ")
    my_nrs = all_numbers[1].split(" ")

    found = 0
    for nr in winning_nrs:
        found += my_nrs.count(nr)

    if found > 1:
        points += pow(2, found-1)
    else:
        points += found
print(points)