data = "data/day1.txt"

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')
    
input_list = read_input(data)

start = 50
result = 0

for element in input_list:
    if element[0] == "R":
        start += int(element[1:])
        if start == 0 or start % 100 == 0:
            result += 1
        else:
            continue

    elif element[0] == "L":
        start -= int(element[1:])
        if start == 0 or start % 100 == 0:
            result += 1
        else:
            continue

print(result)

