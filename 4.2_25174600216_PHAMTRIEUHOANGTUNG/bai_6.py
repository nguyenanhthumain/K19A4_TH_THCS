while True:
    so = int(input("Nhập một số lớn hơn 100: "))
    if so > 100:
        break
    print("Số phải lớn hơn 100. Nhập lại!")

print("CÁCH 1:FOR")
tong_for = 0
for chu_so in str(so):
    tong_for += int(chu_so)
print(f"Tổng các chữ số là: {tong_for}")


print("CÁCH 2:WHILE")
tong_while = 0
temp_so = so
while temp_so > 0:
    tong_while += temp_so % 10
    temp_so //= 10
print(f"Tổng các chữ số là: {tong_while}")