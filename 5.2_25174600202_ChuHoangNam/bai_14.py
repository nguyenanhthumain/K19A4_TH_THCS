#cau14
danh_sach = []
print("Nhap du lieu (Ten,Tuoi,Diem). Nhan Enter trong de dung:")

while True:
    dong = input()
    if not dong: 
        break
    
    thong_tin = dong.split(",")
    ten = thong_tin[0].strip()
    tuoi = int(thong_tin[1].strip())
    diem = int(thong_tin[2].strip())
    
    danh_sach.append((ten, tuoi, diem))

danh_sach.sort()

print("\nDanh sach sau khi sap xep:")
print(danh_sach)