import math
n = int(input())
s = []
for _ in range(n):
    x, y, r = map(int, input().split())
    s.append((x, y, r))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, r1 = s[i]
        x2, y2, r2 = s[j]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance == r1 + r2:
            count += 1
print("\n".join([str(count)]))
