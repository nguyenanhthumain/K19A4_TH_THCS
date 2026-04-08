chuoi_nhap = input("Nhập các tuple (name,age,score) cách nhau bởi dấu cách: ")
danh_sach = []
for item in chuoi_nhap.split():
    ten, tuoi, diem = item.split(',')
    danh_sach.append((ten, int(tuoi), int(diem)))
from operator import itemgetter
danh_sach.sort(key=itemgetter(0, 1, 2))

print("Danh sách sau khi sắp xếp:")
print(danh_sach)