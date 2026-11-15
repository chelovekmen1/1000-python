x, y, x2, y2 = map(int, input().split())
if abs(x-x2) == 1 and abs(y-y2) == 1 or abs(x-x2) == 1 and y == y2 or x == x2 and abs(y-y2) == 1:
    print(1)
else:
    print(0)