def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

m, a = map(int, input().split())
gcd, x, y = gcdExtended(a, m)
if gcd == 1:
    print((x % m + m) % m)
else:
    print(-1)