# Bài 4
"""
Viết chương trình nhập n số dương từ bàn phím. Chương trình sẽ kết thúc
nếu một trong các số đó là số âm.
"""

n = int(input("Nhập n số dương : "))
ds = []
if n > 0 :
    for i in range(1, n + 1) :
        so = int(input(f"Nhập số thứ {i} : "))
        if so < 0 :
            print("Kết thúc chương trình.")
            break
        ds.append(so)
    print("Các số dương đã nhập là : ", ds)
else :
    print("Yêu cầu nhập lại.")  