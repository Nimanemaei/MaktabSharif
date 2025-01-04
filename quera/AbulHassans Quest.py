def main():
    T = int(input())
    results = [] 
    for _ in range(T):
        a, b, r = map(int, input().split())
        if b == 0:
            results.append("Yes" if a == r else "No")
        else:
            results.append("Yes" if (a - r) % b == 0 else "No")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
