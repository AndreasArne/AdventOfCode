# with open("data.txt") as fd:
#     data = fd.read()
data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

data = data.replace("  ", " ")
data = data.splitlines()

def find_winners(lines, stop, start=0):
    points = 0
    for index in range(start, stop):
        whole_line = lines[index]
        JUMP_PAST_SPACE = 2
        start_index = whole_line.index(":")
        all_numbers = whole_line[start_index+JUMP_PAST_SPACE:].split(" | ")
        winning_nrs = all_numbers[0].split(" ")
        my_nrs = all_numbers[1].split(" ")

        found = 0
        for nr in winning_nrs:
            found += my_nrs.count(nr)

        # print(found)
        if found > 0:
            points += 1
            points += find_winners(lines, found, index+1)
    return points

print(find_winners(data, len(data)))