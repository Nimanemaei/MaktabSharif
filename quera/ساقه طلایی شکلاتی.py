n, x, k = map(int, input().split())
if k == 1:
    total_chocolate = 0
else:
    total_chocolate = (k - 1) * x
print(total_chocolate)
