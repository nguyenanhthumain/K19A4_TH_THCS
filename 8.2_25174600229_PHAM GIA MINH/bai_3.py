import random

def la_snt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def bai_3():
    n = int(input())
    ds = [random.randint(1, 100) for _ in range(n)]
    print(ds)
    for x in ds:
        if la_snt(x):
            print(x, end=" ")

if __name__ == "__main__":
    