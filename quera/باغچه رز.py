n, m = map(int, input().split())
flowers = [input().strip() for _ in range(m)]
white_counts = [0] * n
for month in flowers:
    for j in range(n):
        if month[j] == 'W':
            white_counts[j] += 1
result = ''
for count in white_counts:
    if count % 2 == 0:
        result += 'B'
    else:
        result += 'F'
print(result)
