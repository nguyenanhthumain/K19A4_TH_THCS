def fibonacci():
    n = int(input("Nhập số phần tử (<=20): "))

    if n > 20:
        n = 20

    a = 0
    b = 1

    print(a, end=" ")
    if n > 1:
        print(b, end=" ")

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


fibonacci()