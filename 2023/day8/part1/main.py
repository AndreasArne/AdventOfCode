def loop(instructions, node):
    for letter in instructions:
        name = node[letter]
        node = all_nodes[node[letter]]
    return name, node

with open("data.txt") as fd:
    data = fd.read().splitlines()


instructions = data[0]
all_nodes = {}

for node in data[2:]:
    split = node.split(" = ")
    sides = split[1].split(", ")
    all_nodes[split[0]] = {"L": sides[0][1:], "R": sides[1][:-1]}

found = False
loops = 0
current_node = all_nodes["AAA"]
while not found:
    loops += 1
    res = loop(instructions, current_node)
    if res[0] == "ZZZ":
        print(len(instructions)*loops)
        print(res)
        break
    else:
        current_node = res[1]
