def fibonacci():
    n = int(input("Nhập số hạng phần tử: "))
    if n <= 0 or n > 20:
        print("Yêu cầu nhập lại")
        return
    a = 0
    b = 1
    print("Dãy số Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
fibonacci()