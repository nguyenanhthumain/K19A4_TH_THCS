while True:
    n = int(input("Nhập số lớn hơn 100: "))
    if n > 100:
        break
tong = 0
for c in str(n): 
    tong += int(c)

print("Tổng các chữ số là:", tong)