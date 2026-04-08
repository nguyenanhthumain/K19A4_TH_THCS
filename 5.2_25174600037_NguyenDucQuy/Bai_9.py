
nhap_vao = input("Nhập dãy số cách nhau bởi dấu cách: ").split()
ds_so = [int(x) for x in nhap_vao]
try:
    for so in ds_so:
        assert so % 2 == 0, f"Lỗi: Số {so} không phải số chẵn!"
    print("Tất cả các số trong danh sách đều là số chẵn.")
except AssertionError as e:
    print(e)