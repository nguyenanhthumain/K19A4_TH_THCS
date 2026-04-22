#bai4

#a
def P(n):
    t=1
    i=0
    while i<=n:
        t=t*(2*i+1)
        i=i+1
    return t

#b
def S1(n):
    s=0
    i=1
    while i<=n:
        if i%2==0:
            s=s-i
        else:
            s=s+i
        i=i+1
    return s

#c
def S2(n):
    s=0
    i=1
    while i<=n:
        t=0
        j=1
        while j<=i:
            t=t+j
            j=j+1
        s=s+t
        i=i+1
    return s

n=int(input())

print(P(n))
print(S1(n))
print(S2(n))