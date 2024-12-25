n = int(input())
numbers = [float(input()) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if numbers[i] + numbers[j] + numbers[k] == 0:
                count += 1
print(count)
