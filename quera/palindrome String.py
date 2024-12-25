t = input()
is_palindrome = True
length = len(t)
for i in range(length // 2):
    if t[i] != t[length - 1 - i]:
        is_palindrome = False
        break
print(is_palindrome)
