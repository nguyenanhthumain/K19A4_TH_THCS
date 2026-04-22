#bai3
#a
def kiem_tra_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#b
def kiem_tra_hoan_hao(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s==n

#c
def kiem_tra_doi_xung(n):
    return str(n)==str(n)[::-1]

def in_so_doi_xung():
    s=""
    dem=0
    for i in range(1,1000):
        if kiem_tra_doi_xung(i):
            s=s+"{:5}".format(i)
            dem=dem+1
            if dem%15==0:
                s=s+"\n"
    return s

n=int(input())

print(kiem_tra_nguyen_to(n))
print(kiem_tra_hoan_hao(n))
print(in_so_doi_xung())