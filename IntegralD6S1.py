x = int(input("X > "))
y = int(input("Y > "))

a = x // 10
b = x % 10
c = y // 10
d = y % 10
e = 0

A = b + d

if A >= 10:
    A -= 10
    e += 1

B = a + c + e

print(A + 10 * B)