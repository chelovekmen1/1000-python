# N * 1

# a = int(input())
# print(a*4)

# N * 2

# a = float(input())
# print(a**2)

# N * 3

# a, b = map(float, input().split())
# print(a*b, (a+b)*2)

# N * 4

# a = float(input())
# print(a*3.14)

# N * 5

# a = float(input())
# print(a**3, (a**2)*6)

# N * 6

# a, b, c = map(float, input().split())
# print(a*b*c, (a*b + a*c + b*c)*2)

# N * 7

# a = float(input())
# b = a * 2 * 3.14
# s = a**2 * 3.14
# print(f'{b:.2f} {s:.2f}')

# N * 8

# a, b = map(float, input().split())
# print((a+b)/2)

# N * 9

# a, b = map(float, input().split())
# print((a*b)**0.5)

# N * 10

# a, b = map(float, input().split())
# c = (a**2)/(b**2)
# print(f'{a**2+b**2} {a**2-b**2} {a**2*b**2} {c}')

# N * 11

# a = int(input())
# b = int(input())
# print(abs(a)+abs(b))
# print(abs(a)*abs(b))
# print(f'{abs(a)/abs(b):.2f}')

# N * 12

# a = int(input())
# b = int(input())
# print(f'{(a**2+b**2)**0.5:.2f} {(a**2+b**2)**0.5 + a + b:.2f}')

# N * 31

# a = int(input())
# b = (a-32)*5/9
# print(f'{b:.2f}')

# N * 32

# a = int(input())
# b = 9/5*a+32
# print(f'{b:.2f}')

# N * 33

# a, b, c = map(int, input().split())
# e = b/a
# d = e*c
# print(f'{e:.2f} {d:.2f}')

# N * 34

# x, a, y, b = map(int, input().split())
# xx = a/x
# yy = b/y
# if xx>yy:
#     print(f"{xx-yy:.2f} so'm qimmat")
# elif yy>xx:
#     print(f"{yy-xx:.2f} so'm arzon")
# else:
#     print("Teng")

# N * 35

# v1, v2, t1, t2 = map(int, input().split())
# s1 = (v1+v2)*t1
# s2 = (v1-v2)*t2
# s = s1+s2
# print(s)

# N * 36

# v1, v2, s, t = map(int, input().split())
# ss = (v1+v2)*t+s
# print(ss)

# N * 37

# v1, v2, s, t = map(int, input().split())
# ss = abs(s-(v1+v2)*t)
# print(ss)

# N * 38

# a, b = map(int, input().split())
# x = -b/a
# print(f'{x:.2f}')

# N * 39

# a, b, c = map(int, input().split())
# d = b**2-4*a*c
# if d > 0:
#     x1 = (-b+d**0.5)/(2*a)
#     x2 = (-b-d**0.5)/(2*a)
#     if x2>x1:
#         print(f'{x1:.4f} {x2:.4f}')
#     else:
#         print(f'{x2:.4f} {x1:.4f}')
# elif d < 0:
#     print(-1)
# else:
#     x = -b/2*a
#     print(f'{x:.4f}')

# N * 40

# a1, b1, c1 = map(int, input().split())
# a2, b2, c2 = map(int, input().split())
# d = a1*b2 - a2*b1
# dx = c1*b2-c2*b1
# dy = a1*c2-a2*c1
# x = dx/d
# y = dy/d
# print(f'{x:.2f} {y:.2f}')

# N * 41

# a = int(input())
# b = 1
# for i in range(2, a + 1):
#     b*=i
# print(b)

# N * 42

# a = input()
# b = 0
# for i in a:
#     b+=1
# print(b)

# N * 43

# a, b, c = map(int, input().split())
# d = [a, b, c]
# print(max(d))

# N * 44

# a, b = map(int, input().split())
# if a%2==1 or b%2==1:
#     print("YES")
# else:
#     print("NO")

# N * 45

# a = input()
# if a == 'Dushanba':
#     print(1)
# elif a == 'Seshanba':
#     print(2)
# elif a == 'Chorshanba':
#     print(3)
# elif a == 'Payshanba':
#     print(4)
# elif a == 'Juma':
#     print(5)
# elif a == 'Shanba':
#     print(6)
# elif a == 'Yakshanba':
#     print(7)

# N * 46

# a = int(input())
# b = a // 100
# print(b)

# N * 47

# a = int(input())
# b = a // 1000
# print(b)

# N * 48

# a = int(input())
# b = a // 1024
# print(b)

# N * 49

# a, b = map(int, input().split())
# print(a // b)

# N * 50

# a, b = map(int, input().split())
# print(a % b)

# N * 51

# a = int(input())
# print(a//10, a%10)

# N * 52

# a = int(input())
# a1 = a // 10
# a2 = a % 10
# print(a1+a2, a1*a2)

