a, b = map(int, input().split())
if a != b:
    b = max(a, b)
    a = b
else:
    a = 0
    b = 0
print(a, b)