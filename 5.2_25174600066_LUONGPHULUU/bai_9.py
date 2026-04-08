lst = list(map(int, input("Nhập các số: ").split()))
for x in lst:
    assert x % 2 == 0, "Danh sách có số lẻ!"
print("Tất cả các số đều là số chẵn.")