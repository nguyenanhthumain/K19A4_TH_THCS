#bai_3
"""
Viết chương trình nhập vào một danh sách các phần tử là số tự nhiên (bao gồm cả
phần âm và dương) cho đến khi nhập vào số 0. Thực hiện các yêu cầu sau:
a. Viết chương trình chuyển các phần tử dương lên đầu danh sách và in danh sách
đó ra màn hình.
b. Chèn một số m (nhập từ bàn phím) vào đầu danh sách, cuối danh sách và vị trí
thứ 5 của danh sách.
"""

n = int(input("Nhập số phần tử của danh sách: "))
ds = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ds.append(phan_tu)
       

#a 
phan_tu_duong = []
phan_tu_am = []
for i in ds:
    if i > 0:
        phan_tu_duong.append(i)
    else:
        phan_tu_am.append(i)
phan_tu = phan_tu_duong + phan_tu_am
print("Danh sách sau khi chuyển là : ", phan_tu)


#b
m = int(input("Nhập số m: "))
ds.insert(0, m)
ds.append(m)
if len(ds) >= 5:
    ds.insert(4, m)
print("Danh sách sau khi chèn là: ", ds)