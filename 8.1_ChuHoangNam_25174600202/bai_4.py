#cau4
#a
def tinh_p_4a():
    n = int(input("Nhap n: "))
    p = 1
    for i in range(n + 1):
        term = 2 * i + 1
        p = p * term
    print("Ket qua p:", p)
tinh_p_4a()

#b
def tinh_s_4b():
    n = int(input("Nhap n: "))
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s = s - i  
        else:
            s = s + i  
    print("Ket qua s:", s)
tinh_s_4b()

#c
def tinh_s_4c():
    n = int(input("Nhap n: "))
    s = 0
    sub_sum = 0 
    
    for i in range(1, n + 1):
        sub_sum = sub_sum + i 
        s = s + sub_sum       
    print("Ket qua s:", s)
tinh_s_4c()

#d
def tinh_p_4d():
    x = int(input("Nhap x: "))
    y = int(input("Nhap y: "))
    n = int(input("Nhap n: "))
    
    res = x ** y
    
    for k in range(1, n + 1):
        term = x + (32 * y) + (y ** k)
        res = res + term
    print("Ket qua p:", res)
tinh_p_4d()