def fibonacci():
    n = int(input("Nhập số phần tử (<=20): "))

    if n <= 0 or n > 20:
        print("Không hợp lệ!")
        return

    a, b = 0, 1
    print("Dãy Fibonacci:", end=" ")

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci()