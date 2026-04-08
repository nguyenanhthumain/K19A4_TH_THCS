nhap = input("Nhập các số chẵn:  ")
danh_sach = [int(x) for x in nhap.split()]

for x in danh_sach:
    assert x%2==0, f"Số {x} không phải số chẵn!"

print("Tất cả các số đều là số chẵn.")