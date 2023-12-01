import re
with open("data.txt") as fd:
    data = fd.readlines()
replaces = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "th3ree",
    "four": "f4our",
    "five": "fi5ve",
    "six": "s6ix",
    "seven": "se7ven",
    "eight": "ei8ght",
    "nine": "n9ine",
}

replace_pattern = re.compile("|".join(re.escape(key) for key in replaces.keys()))

text = ""
for line in data:
    for key, value in replaces.items():
        line = line.replace(key, value)
    text += line
pattern = re.compile(r"^[a-z]*(\d).*(\d)[a-z]*$|\D*(\d)\D*$", flags=re.M) # \D = Inte siffra

matches = pattern.findall(text)

sum = 0
for match in matches:
    if match[2]:
        sum += int(match[2] + match[2])
    else:
        number = match[0] + match[1]
        sum += int(number)

print(sum)
