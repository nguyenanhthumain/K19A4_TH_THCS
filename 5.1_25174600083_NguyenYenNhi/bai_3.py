#bai_3
"""
Viết chương trình có thể lọc các số chẵn trong danh sách sử dụng hàm filter. Danh
sách là các số tự nhiên liên tục từ m đến n với 0 < m < n được nhập từ bàn phím.
Lưu ý kiểm tra điều kiện của m và n, nếu không thoả mãn thì báo lỗi và yêu cầu
nhập lại.
"""

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
if 0 < m < n :
    List = []
    for i in range(m , n + 1) :
        List.append(i)
    a = list(filter(lambda x: x % 2 == 0, List))
    print("Danh sách các số chẵn từ m đến n là : ", a)
else:
    print("Lỗi . Vui lòng nhập lại.")
