# bai2 - in day fibonacci
def day_fibonacci():
    n=int(input())
    if n>20:
        n=20
    a=0
    b=1
    i=0
    s=""
    while i<n:
        s=s+str(a)+" "
        c=a+b
        a=b
        b=c
        i=i+1
    return s

kq=day_fibonacci()
print(kq)