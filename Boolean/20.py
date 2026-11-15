a, b, c = map(float, input().split())
ab = abs(b - a)
ac = abs(c - a)
if ab<ac:
    print(b, ab)
else:
    print(c, ac)