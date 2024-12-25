n = int(input())
numbers = []
min1 = float('inf')
min2 = float('inf')
for _ in range(n):
    number = int(input())
    numbers.append(number)
    if number < min1:
        min2 = min1
        min1 = number
    elif number < min2 and number != min1:
        min2 = number
print(min1)
print(min2)
print(numbers)
