"""Bài 4. Hãy viết một hàm để đảo ngược một danh sách được nhập từ bàn phím."""

def dao_nguoc_danh_sach(danh_sach):
    return danh_sach[::-1]

n = int(input("Nhập số phần tử của danh sách: "))
danh_sach = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(x)

print("Danh sách ban đầu:", danh_sach)
print("Danh sách sau khi đảo ngược:", dao_nguoc_danh_sach(danh_sach))