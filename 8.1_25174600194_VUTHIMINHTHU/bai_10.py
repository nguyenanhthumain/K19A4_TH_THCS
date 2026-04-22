def nhap_n():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            return n
        print("Vui lòng nhập một số lớn hơn 0!")
n = nhap_n()
print(f"Các ước số của {n} là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
