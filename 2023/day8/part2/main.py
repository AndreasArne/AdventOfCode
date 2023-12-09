def loop(instructions, node):
    for letter in instructions:
        name = node[letter]
        node = all_nodes[node[letter]]
    return name, node



with open("data.txt") as fd:
    data = fd.read().splitlines()

instructions = data[0]
all_nodes = {}
starting_nodes = []

for node in data[2:]:
    split = node.split(" = ")
    sides = split[1].split(", ")
    all_nodes[split[0]] = {"L": sides[0][1:], "R": sides[1][:-1]}
    if split[0][2] == "A":
        starting_nodes.append(all_nodes[split[0]])

found = False
loops = 0
while not found:
    loops += 1
    results = []
    for current_node in starting_nodes: 
        results.append(loop(instructions, current_node))
    # input(results)
    if all([res[0][2] == "Z" for res in results]):
        print(len(instructions)*loops)
        print(results)
        break
    else:
        starting_nodes = [res[1] for res in results]
