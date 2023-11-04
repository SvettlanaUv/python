import scipy.misc as sc
import math

def F(x):
    return math.exp(x)


def Teilor(k, a, f, eps):
    teil_sec = []
    for n in range(0, k):
        teil_sec.append(sc.derivative(f, a, eps)/math.factorial(n))
    return sum(teil_sec)


print(Teilor(150, 0, F, 0.000001))

