with open('day2.txt', 'r') as f:
    input = f.read().strip().split(',')

ranges = []

for item in input:
    parts = item.split('-')
    a = int(parts[0])
    b = int(parts[1])
    ranges.append(list(range(a, b + 1)))

def check_repetition(n):
    s = str(n)
    length = len(s)
    
    for factor in range(1, length // 2 + 1):
        if length % factor != 0:
            continue
            
        blobs = [s[i:i+factor] for i in range(0, length, factor)]
        
        if len(set(blobs)) == 1:
            return True
            
    return False

result = 0

for r in ranges:
    for number in r:
        if check_repetition(number):
            result += number

print(result)
