# a. Tạo và in
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("7a. Danh sách List_:", List_)

# b. Chọn phần tử thứ 2, thuộc vị trí thứ 3 của sublist
# Lưu ý: List_ chỉ có 7 sublist, mỗi sublist có 2 phần tử. 
# Có lẽ đề yêu cầu sublist thứ 3, phần tử thứ 2?
val = List_[2][1] 
print("7b. Phần tử tại sublist 3, vị trí 2:", val)

# c. Thêm sublist ngẫu nhiên
List_.append(["new", 100])
print("7c. Độ dài sau khi thêm:", len(List_))

# d. Tổng sale value (mon, tue, sat, sun)
targets = ["mon", "tue", "sat", "sun"]
tong_sale = sum([item[1] for item in List_ if item[0] in targets])
print("7d. Tổng sale (Thứ 2, 3, 7, CN):", tong_sale)