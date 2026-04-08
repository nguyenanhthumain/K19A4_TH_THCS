"""Giả sử có một danh sách như sau: List _= [["'mon", 73], ["tue", 89], ["wed", 95],
["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]. Yêu cầu:
a. Tạo danh sách List_ và in các phần tử của List_ ra màn hình
b. Chọn ra phần từ thứ hai, thuộc vị trí thứ 3 của sublist.
c. Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên.
d. Thực hiện tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và
chủ nhật."""

#a
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:", List)

#b
phan_tu = List[2][1]
print("Phần tử yêu cầu (thứ 2 của sublist thứ 3):", phan_tu)

#c
List.append(["new", 100])
print("Sau khi thêm:", List)

#d
tong_sale = 0
ngay_can_tinh = ["mon", "tue", "sat", "sun"]
for sub in List:
    if sub[0] in ngay_can_tinh:
        tong_sale += sub[1]
print("Tổng sale value các ngày yêu cầu:", tong_sale)