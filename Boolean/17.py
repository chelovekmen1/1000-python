a, b, c = map(float, input().split())
if a < b < c or a > b > c:
    print(a*2, b*2, c*2)
else:
    print(-a, -b, -c)