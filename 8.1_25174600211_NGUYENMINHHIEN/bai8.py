def tron():
    r = float(input("r: "))
    if r>0:
        print("CV:", 2*3.14*r, "DT:", 3.14*r*r)
def vuong():
    a = float(input("a: "))
    if a>0:
        print("CV:", 4*a, "DT:", a*a)
def hcn():
    a = float(input("a: "))
    b = float(input("b: "))
    if a>0 and b>0:
        print("CV:", 2*(a+b), "DT:", a*b)
def tg():
    a,b,c = float(input()), float(input()), float(input())
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        print("CV:", a+b+c, "DT:", (p*(p-a)*(p-b)*(p-c))**0.5)
tron()
vuong()
hcn()
tg()