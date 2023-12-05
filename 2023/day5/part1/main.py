def parse_mappings(sections):
    parsed_sections = []
    for section in sections:
        ranges = section.split("\n")[1:] # ignore name of section
        for range in ranges:
            numbers = range.split(" ")
            dest = int(numbers[0]) # for readability
            src = int(numbers[1])
            len_ = int(numbers[2])-1
            parsed_sections.append((src, src+len_, dest, dest+len_))
    return parsed_sections

with open("data.txt") as fd:
    data = fd.read()


sections = data.split("\n\n")
seeds = map(int, sections[0].split(" ")[1:])
mappings = parse_mappings(sections[1:])

for seed in seeds:
    src = seed
    for mapping in mappings:
        if mapping[0] <= src >= mapping[1]:
            # ersätt src med motsvarande dest.
            print(src, mapping, "if")
            exit()
        else:
            print(src, mapping, "else")
print(seeds, mappings)

