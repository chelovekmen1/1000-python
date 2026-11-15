a = int(input())
if a % 100 != 0 and a % 4 == 0 or a % 100 == 0 and a % 400 == 0:
    print(366)
else:
    print(365)