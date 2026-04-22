#bai_4
"""
Hãy viết một hàm để đảo ngược một danh sách được nhập từ bàn phím.
"""

def dao_nguoc_ds(danh_sach):
    return danh_sach[::-1]
n = int(input("Nhập độ dài của danh sách: "))
ds = []
for i in range(n):
    so_phan_tu = input(f"Nhập phần tử thứ {i+1}: ")
    ds.append(so_phan_tu)
ds_dao_nguoc = dao_nguoc_ds(ds)
print("Danh sách sau khi đảo ngược:", ds_dao_nguoc)