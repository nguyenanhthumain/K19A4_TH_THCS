# bai 1
# for
n = int(input("Nhập một số nguyên: "))
if n <= 0 :
    print("Yêu cầu nhập lại")
else :
    S1 = 0 
    for i in range(1, n+1) :
        S1 = S1 + i ** 2
    print("Tổng S1 = ", S1)

    S2 = 0
    for i in range(1, n+1) :
        S2 = S2 + (2*(i-1) +1) ** 3    
    print("Tổng S2 = ", S2)

    S3 = 0
    for i in range(1 , n+1) :
        S3 = S3 + (2*n) ** 4
    print("Tổng S3 = ", S3)

    S4 = 0
    for i in range(1 , n+1) :
        S4 = S4 + ((-1)**(i-1)) / i
    print("Tổng S4 = ", S4)

    S5 = 0 
    for i in range(1 , n+1) :
        S5 = S5 + 1 / (i * (i+1))
    print("Tổng S5 = ", S5)

    S6 = 0
    for i in range(1 , n+1) :
        S6 = S6 + 1/ (i ** 0.5)
    print("Tổng S6 = ", S6)
# while
n = int(input("Nhập một số nguyên: "))  
if n <= 0 :
    print("Yêu cầu nhập lại")   
else :
    S1 = S2 = S3 = S4 = S5 = S6 = 0
    i = 1
    while i <= n :
        S1 = S1 + i ** 2
        S2 = S2 + (2*(i-1) +1) ** 3
        S3 = S3 + (2*n) ** 4
        S4 = S4 + ((-1)**(i-1)) / i
        S5 = S5 + 1 / (i * (i+1))
        S6 = S6 + 1/ (i ** 0.5)
        i += 1
    print("Tổng của S1 = ", S1)
    print("Tổng của S2 = ", S2)     
    print("Tổng của S3 = ", S3)
    print("Tổng của S4 = ", S4)
    print("Tổng của S5 = ", S5)
    print("Tổng của S6 = ", S6)