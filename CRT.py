
 
import os
 
N = 100010
n = 0
m = 0
 
def Exgcd(r0, r1): # calc ax+by = gcd(a, b) return x
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    x, y = r0, r1
    r = r0 % r1
    q = r0 // r1
    while r:
        x, y = x0 - q * x1, y0 - q * y1
        x0, y0 = x1, y1
        x1, y1 = x, y
        r0 = r1
        r1 = r
        r = r0 % r1
        q = r0 // r1
    return x
 
def __gcd(x, y):
    if y:
        return __gcd(y, x%y)
    else:
        return x
 
def fp(x, y, MOD):
    res = 0
    while y:
        if y%2 == 1:
            res = res + x
        res %= MOD
        x += x
        x %= MOD
        y //= 2
    return res
 
def excrt():
    x = 0
    y = 0
    k = 0
    M = b[0]
    ans = a[0]
    for i in range(1, n):
        A = M
        B = b[i]
        C = (a[i] - ans%B + B) % B
        # print(A, B, C)
        gcd = __gcd(A, B)
        x = Exgcd(A, B)
        # x = (x + B) % B
        # print(x)
        B //= gcd
        if C % gcd:
            return -1
        # print(x, C, gcd, B)
        x = fp(x, C // gcd, B)
        # print(x)
        ans += x * M
        M *= B
        ans = (ans%M + M) % M
    return (ans%M + M) % M
 
a = []
b = []
n,m = map(int,input().split())
for i in range(N):
    b.append(0)
    a.append(0)
flag = True
for i in range(n):
    b[i], a[i] = map(int, input().split())
    if a[i] != 0:
        flag = False
ans=excrt()
if ans==-1:
    print("he was definitely lying")
elif ans>m:
    print("he was probably lying")
else:
    print(ans)
