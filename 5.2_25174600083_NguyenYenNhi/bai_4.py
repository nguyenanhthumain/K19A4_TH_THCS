#bai_4
"""
Viết chương trình nhập vào một danh sách (list) các phần tử là số tự nhiên (có thể
nhận giá trị âm và dương) cho đến khi nhập vào số 0. Thực hiện các yêu cầu sau:
a. Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
b. Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
c. Sắp xếp danh sách theo thứ tự tăng dần, giảm dần.
"""

n = int(input("Nhập số phần tử của danh sách: "))
ds_list = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ds_list.append(phan_tu)

#a 
ds = [1, 2, 3] + ds_list + [1, 2, 3]
if len(ds) >= 5:
    ds[4:4] = [1, 2, 3]
print(f"Danh sách sau khi chèn: {ds}")

#b
k = int(input("Nhập phần tử thứ k : "))
if 0 <= k < len(ds) :
    ds_moi = ds[:k] + ds[k+1:]
    print(f"Danh sách sau khi xóa phần tử thứ {k}: {ds_moi}")
else:
    print("Vị trí k không hợp lệ.")

#c
for i in range(len(ds)) :
    for j in range(i + 1, len(ds)) :
        if ds[i] > ds[j] :
            ds[i], ds[j] = ds[j], ds[i]
print(f"Danh sách sau khi sắp xếp tăng dần: {ds}")
for i in range(len(ds)) :
    for j in range(i + 1, len(ds)) :
        if ds[i] < ds[j] :
            ds[i], ds[j] = ds[j], ds[i]
print(f"Danh sách sau khi sắp xếp giảm dần: {ds}")