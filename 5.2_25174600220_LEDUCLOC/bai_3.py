"""3. Viết chương trình nhập vào một danh sách các phần tử là số tự nhiên (bao gồm cả
phần âm và dương) cho đến khi nhập vào số 0. Thực hiện các yêu cầu sau:
a. Viết chương trình chuyển các phần tử dương lên đầu danh sách và in danh sách
đó ra màn hình.
b. Chèn một số m (nhập từ bàn phím) vào đầu danh sách, cuối danh sách và vị trí
thứ 5 của danh sách."""

a = []
while True:
    x = int(input("Nhập phần tử: "))
    if x == 0:
        break
    a.append(x)
print(f"Danh sách vừa nhập là: {a}")

# a
duong = []
am = []
for i in a:
    if i > 0:
        duong.append(i)
    else:
        am.append(i)
print(f"Danh sách các số dương là: {duong}")
print(f"Danh sách các số âm là: {am}")

# b
m = int(input("Nhập số m: "))
a.insert(0, m)
a.insert(len(a), m)
a.insert(4, m)
print(a)
