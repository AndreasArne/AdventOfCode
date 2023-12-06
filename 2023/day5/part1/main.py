def parse_mappings(sections):
    parsed_sections = []
    for section in sections:
        ranges = section.split("\n")[1:] # ignore name of section
        section = []
        for range in ranges:
            numbers = range.split(" ")
            # for readability
            dest = int(numbers[0])
            src = int(numbers[1])
            len_ = int(numbers[2])-1
            section.append((src, src+len_, dest, dest+len_))
        parsed_sections.append(section)
    return parsed_sections

with open("data.txt") as fd:
    data = fd.read()


sections = data.split("\n\n")
seeds = map(int, sections[0].split(" ")[1:])
mappings = parse_mappings(sections[1:])
locations = []
for seed in seeds:
    src = seed
    for mapping in mappings:
        found = False
        for section in mapping:
            if section[0] <= src <= section[1]:
                found = True
                break
        if found:
            diff = src-section[0]
            src = section[2]+diff
    locations.append(src)
print(min(locations))
