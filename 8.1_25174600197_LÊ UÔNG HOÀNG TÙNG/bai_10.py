def uoc_so(n):
    print("cac uoc cua", n, ":")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
def bai_10():
    n = int(input("nhap n: "))
    uoc_so(n)
bai_10()