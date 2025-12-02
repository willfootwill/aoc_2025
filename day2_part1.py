with open('day2.txt', 'r') as f:
    input = f.read().strip().split(',')

ranges = []

for item in input:
    parts = item.split('-')
    a = int(parts[0])
    b = int(parts[1])
    ranges.append(list(range(a, b + 1)))

#print(ranges)

def check_repetition(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
       return False
    mid = length // 2 
    left_half = s[:mid]
    right_half = s[mid:]
    
    return left_half == right_half

result = 0

for r in ranges:
    for number in r:
        if check_repetition(number):
            result += number

print(result)
