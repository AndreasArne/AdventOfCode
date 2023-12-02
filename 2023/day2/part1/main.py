import re

MAX_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def too_many(game):
    for stones in game:
        nr, color = stones.split(" ")
        if int(nr) > MAX_COLORS[color]:
            return True
    return False

with open("data.txt") as fd:
    data = fd.read()
    data = data.split("\n")

id_sum = 0
for line in data:
    game_nr, games = line.split(": ")
    games = games.split("; ")
    print(games, game_nr)
    enough = True
    for game in games:
        game = game.split(", ")
        print(game)
        if too_many(game):
            enough = False
            break
    if enough:
        id_sum += int(game_nr.replace("Game ", ""))
print(id_sum)