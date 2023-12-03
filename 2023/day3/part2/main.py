from functools import reduce

with open("data.txt") as fd:
    data = fd.read()

LEN = 141
found_gears = {}

def is_symbol(index, nr, data):
    try:
        if data[index] == "*":
            found_gears.setdefault(index, []).append(nr)
    except IndexError:
        pass

def check_for_symbols(start, end, nr, data):
    is_symbol(start-1, nr, data)
    is_symbol(end, nr, data)
    for i in range(start-LEN-1, end-LEN+1): # above
        is_symbol(i, nr, data)
    for i in range(start+LEN-1, end+LEN+1): # below
        is_symbol(i, nr, data)


start = -1
end = -1
for index, char in enumerate(data):
    if start < 0 and char.isdigit():
        start = index
    elif start >=0 and not char.isdigit():
        end = index
        nr = int(data[start:end])
        check_for_symbols(start, end, nr, data)
        start = -1
        end = -1

sum_ = 0
for index, nrs in found_gears.items():
    print(nrs)
    if len(nrs) == 2:
        sum_ += reduce(lambda x, y: x*y, nrs)
print(sum_)


