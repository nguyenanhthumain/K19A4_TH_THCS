def dao_nguoc_danh_sach(danh_sach):
    n = len(danh_sach)
    for i in range(n // 2):
        # Hoán đổi
        danh_sach[i], danh_sach[n - 1 - i] = danh_sach[n - 1 - i], danh_sach[i]
    return danh_sach
ds = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
ds_dao = dao_nguoc_danh_sach(ds)
print("Danh sách sau khi đảo:", ds_dao)