a, b, c = map(int, input().split())
k = 0
k2 = 0
if a > 0:
    k += 1
elif a < 0:
    k2 += 1
if b > 0:
    k += 1
elif b < 0:
    k2 += 1
if c > 0:
    k += 1
elif c < 0:
    k2 += 1
print(k, k2)