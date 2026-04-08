import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Các phần tử trong List_:")
for item in List_:
    print(item)
gia_tri = List_[2][1]
print(f"Phần tử yêu cầu: {gia_tri}")
print(f"Độ dài hiện tại: {len(List_)}")
List_.append(["new_day", random.randint(50, 150)])
print("Danh sách sau khi thêm ngẫu nhiên:", List_)
chi_so_ngay = [0, 1, 5, 6]
tong_sale = sum(List_[i][1] for i in chi_so_ngay)
print(f"Tổng sale value các ngày yêu cầu: {tong_sale}")