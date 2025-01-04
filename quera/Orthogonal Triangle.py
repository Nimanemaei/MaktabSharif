def squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def triangle(p1, p2, p3):
    a2 = squared(p1, p2)
    b2 = squared(p2, p3)
    c2 = squared(p1, p3)
    sides_squared = sorted([a2, b2, c2])
    return sides_squared[0] + sides_squared[1] == sides_squared[2]

def solve():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if triangle(points[i], points[j], points[k]):
                    count += 1
    print(count)

solve()