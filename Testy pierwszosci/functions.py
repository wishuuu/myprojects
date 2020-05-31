import math
import random
import matplotlib.pyplot as plt

def naive1(n):
    if n == 2:
        return True
    if n in [0, 1]:
        return False

    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

def naive2(n):
    if n == 2:
        return True
    if n in [0, 1]:
        return False

    i = 2
    limit = int(math.sqrt(n))
    while i < limit:
        if n%i == 0:
            return False
        i += 1
    return True

def wilson(n):
    if n == 1:
        return False
    return (math.factorial(n-1)+1)%n==0

"""
Algorytm oparty o Małe Twierdzenie Fermata sprawdzam dla 10 losowych liczb naturnalnych w przedziale <2,p-1>, gdzie p to rozpatrywana liczba
"""
def fermat(n):
    for _ in range(10):
        a = random.randint(2,n-1)
        if pow(a,n-1)%n!=1: return False
    return True

def show_chart(x, y, x0=1, y0=1):
    points = []
    for i in range(x-x0+1):
        for j in range(y-y0+1):
            if (j+y0)%(i+x0)==0: points.append([i+x0,j+x0])
    plt.scatter([point[0] for point in points], [point[1] for point in points])
    plt.show()
