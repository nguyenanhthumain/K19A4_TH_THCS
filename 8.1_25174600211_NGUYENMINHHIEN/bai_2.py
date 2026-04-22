def fibonacci():
    n = int(input("Nhap so luong (<=20): "))
    if n > 20:
        n = 20
    a, b = 0, 1
    print(a, end=" ")
    if n > 1:
        print(b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
fibonacci()