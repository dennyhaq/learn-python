
kali = lambda a, b : a * b

print(kali(12,21))


def factorial(n):
    if n==1: return 1
    return (n*factorial(n-1))

a1=(factorial(40))



def faktor(n):
    if n==1: return 1
    return (n*faktor(n-1))
print (a1*faktor(int(input())))


def fpb(a, b):
    while b:
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)

# Contoh penggunaan
a = 1120
b = 1480

print(f"FPB dari {a} dan {b} adalah {fpb(a, b)}")
print(f"KPK dari {a} dan {b} adalah {kpk(a, b)}")