# Nhập danh sách
inp = input("Nhập các số cách nhau bởi dấu cách: ")
a = [int(x) for x in inp.split()]

# Kiểm tra bằng assert
for x in a:
    assert x % 2 == 0, f"Số {x} không phải là số chẵn!"

print("Tất cả các số đều là số chẵn.")