def uoc_so(n):
    if n <= 0:
        print("Phải nhập số nguyên dương!")
        return
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

try:
    n = int(input("Nhập n: "))
    uoc_so(n)
except:
    print("Lỗi: phải nhập số nguyên!")