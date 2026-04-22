def in_fibonacci():
    n = int(input("Nhập số lượng số Fibonacci (<=20): "))
    if n <= 0 or n > 20:
        print("Vui lòng nhập n trong khoảng 1 đến 20")
        return
    a = 0
    b = 1
    print("Dãy Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
in_fibonacci()