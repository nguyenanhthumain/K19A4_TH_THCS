def day_fibonacci():
    n = int(input("nhap so luong phan tu (ko qua 20): "))
    if n > 20:
        n = 20
    a = 0
    b = 1
    print("day fibonacci:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
day_fibonacci()