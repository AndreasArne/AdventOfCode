import re
with open("data.txt") as fd:
    data = fd.read()

pattern = re.compile(r"^[a-z]*(\d).*(\d)[a-z]*$|\D*(\d)\D*$", flags=re.M)

matches = pattern.findall(data)

sum = 0
for match in matches:
    if match[2]:
        sum += int(match[2] + match[2])
    else:
        number = match[0] + match[1]
        sum += int(number)

print(sum)
