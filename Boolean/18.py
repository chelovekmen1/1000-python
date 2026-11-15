a, b, c = map(int, input().split())
if a != b and a != c:
    print(1)
elif b != a and b != c:
    print(2)
elif c != a and c != b:
    print(3)