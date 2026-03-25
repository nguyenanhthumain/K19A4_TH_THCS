"""Bài 10: Viết chương trình in tất cả các số nguyên tố từ 1 đến n được nhập từ bàn phím.
Viết chương trình in tất cả các số hoàn hảo từ 1 đến n được nhập từ bàn phím."""
n = int(input("Nhập một số nguyên dương: "))
if n > 1:
    print("Các số nguyên tố từ 1 đến", n, "là:")
    for a in range(2, n + 1):
        m = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                m = False
                break
        if m:
            print(a, end=' ')