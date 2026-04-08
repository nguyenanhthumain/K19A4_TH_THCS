ds = []
while True:
    so = int(input("Nhập số (nhập 0 để dừng): "))
    if so == 0:
        break
    ds.append(so)
ds_duong = [x for x in ds if x > 0]
ds_am_khong = [x for x in ds if x <= 0]
ds_moi = ds_duong + ds_am_khong
print(f"Danh sách sau khi sắp xếp lại: {ds_moi}")
m = int(input("Nhập số m cần chèn: "))
ds.insert(0, m)
ds.append(m)
if len(ds) >= 5:
    ds.insert(4, m) 
else:
    print("Danh sách không đủ 5 phần tử để chèn vào vị trí thứ 5.")

print(f"Danh sách cuối cùng: {ds}")