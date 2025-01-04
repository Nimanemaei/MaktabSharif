def minimal_price(n, prices):
    prices.sort(reverse=True)
    total_price = 0
    for i in range(n):
        total_price += prices[i]
        if (i + 1) % 3 == 0:
            total_price -= prices[i]  
    return total_price
n = int(input())
prices = list(map(int, input().split()))
print(minimal_price(n, prices))
