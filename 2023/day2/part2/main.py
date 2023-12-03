from functools import reduce

def multiply_all(lst):
    return reduce(lambda x, y: int(x) * int(y), lst, 1)

with open("data.txt") as fd:
    data = fd.read()
    data = data.split("\n")

id_sum = 0
for line in data:
    game_nr, games = line.split(": ")
    games = games.split("; ")
    enough = True

    max_colors = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    for game in games:
        game = game.split(", ")
        for stone in game:
            nr, name = stone.split(" ")
            if max_colors[name] < int(nr):
                max_colors[name] = int(nr)
    id_sum += multiply_all(max_colors.values())

print(id_sum)