
with open("data.txt") as fd:
    data = fd.read()

LEN = 141

def is_symbol(index, data):
    try:
        return not data[index] in ".\n" and not data[index].isdigit()
    except IndexError:
        pass
    return False

def check_for_symbols(start, end, data):
    if is_symbol(start-1, data) or is_symbol(end, data):
        return True
    for i in range(start-LEN-1, end-LEN+1): # above
        if is_symbol(i, data):
            return True
    for i in range(start+LEN-1, end+LEN+1): # below
        if is_symbol(i, data):
            return True
    return False


start = -1
end = -1
sum_ = 0
for index, char in enumerate(data):
    if start < 0 and char.isdigit():
        start = index
    elif start >=0 and not char.isdigit():
        end = index
        if check_for_symbols(start, end, data):
            print(True)
            sum_ += int(data[start:end])
        else:
            print(False)
        start = -1
        end = -1
print(sum_)


