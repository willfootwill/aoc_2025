data = "data/day1.txt"

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')
    
input_list = read_input(data)

start = 50
progression = [50]
result = 0

for element in input_list:
    if element[0] == "R":
        start += int(element[1:])
        progression.append(start)


    elif element[0] == "L":
        start -= int(element[1:])
        progression.append(start)
        


for element in progression:
    if element == 0 or element % 100 == 0:
        result += 1

for r in range(len(progression) - 1):
    start = progression[r]
    end = progression[r+1]
    
    if start < end:
        step = 1
    else:
        step = -1
        
    for position in range(start + step, end, step):
        if position == 0 or position % 100 == 0:
            result += 1

print(result)
