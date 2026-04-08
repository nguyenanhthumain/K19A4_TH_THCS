n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input("Nhập phần tử thứ {}: ".format(i))))
    
#a
tong = 0
for x in a:
    tong += x
print("Tổng các phần tử:", tong)

#b
count_duong = 0
sum_duong = 0
for x in a:
    if x > 0:
        count_duong += 1
        sum_duong += x
print("Số lượng số dương:", count_duong)
print("Tổng các số dương:", sum_duong)

#c
vi_tri_am = -1
for i in range(n):
    if a[i] < 0:
        vi_tri_am = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am)

#d
vi_tri_duong_cuoi = -1
for i in range(n-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)

#e
max_val = a[0]
vi_tri_max = 0
for i in range(n):
    if a[i] >= max_val:
        max_val = a[i]
        vi_tri_max = i
print("Phần tử lớn nhất:", max_val)
print("Vị trí cuối cùng của phần tử lớn nhất:", vi_tri_max)