#bai_7
"""
Giả sử có một danh sách như sau: List _= [["'mon", 73], ["tue", 89], ["wed", 95],
["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]. Yêu cầu:
a. Tạo danh sách List_ và in các phần tử của List_ ra màn hình
b. Chọn ra phần từ thứ hai, thuộc vị trí thứ 3 của sublist.
c. Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên.
d. Thực hiện tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và
chủ nhật.
"""

List= [["'mon", 73], ["tue", 89], ["wed", 95],["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
#a
print("Danh sách List_ là: ", List )
#b
phan_tu = List[2][1]
print("Phần tử thứ hai, thuộc vị trí thứ 3 của sublist là: ", phan_tu)
#c
print("Độ dài của list test là: ", len(List))   
sublist_moi = ["a", 150]
List.append(sublist_moi)
print("Danh sách List_ sau khi thêm sublist mới là: ", List)
#d
tong_sale_value = List[1][1] + List[2][1] + List[5][1] + List[6][1]
print("Tổng sale value là: ", tong_sale_value)