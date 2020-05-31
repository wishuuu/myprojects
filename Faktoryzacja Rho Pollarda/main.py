import random
import math

def is_prime(n):
    if n == 2:
        return True
    if n in [0,1]:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

def NWD(x,y):
    while y!=0:
        pom=y
        y=x%y
        x=pom
    return x
"""
Definiuję stałą funkcję f()=x^2+1 dla zapewnienia czytelności kodu.
Algorytm Rho Pollarda nie jest w stanie poprawnie rozłożyć niektórych liczb na czynniki pierwsze, a liczby te są zależne od postaci funkcji f().
Dla przyjętej przeze mnie problem stanowią między innymi liczby będące iloczynami 2 oraz 5
"""
def f(n):
    return n**2+1

def rho_pollard(n):
    x=2
    y=2
    d=1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = NWD(math.fabs(x-y), n)
    return None if d == n else d

print("Podaj liczbe")
n = int(input())
if is_prime(n):
    print([n])
else:
    c = 1
    tab = []
    while 1:
        c = rho_pollard(n)
        if c != None:
            tab.append(c)
            n /= c
        else:
            tab.append(n)
            break
    print(tab)
