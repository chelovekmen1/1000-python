a, b = map(int, input().split())
if a != b:
    a = a + b
    b = a
else:
    a = 0
    b = 0
print(a, b)