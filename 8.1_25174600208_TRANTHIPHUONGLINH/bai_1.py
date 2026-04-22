#bai1 - tinh luy thua
def tinh_luy_thua():
    x=int(input())
    n=int(input())
    kq=1
    for i in range(n):
        kq=kq*x
    return kq

print(tinh_luy_thua())