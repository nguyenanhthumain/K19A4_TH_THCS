#Bài 3. Viết chương trình có thể lọc các số chẵn trong danh sách sử dụng hàm filter. Danh sách là các số tự nhiên liên tục từ m đến n với 0 < m < n được nhập từ bàn phím.Lưu ý: kiểm tra điều kiện của m và n, nếu không thoả mãn thì báo lỗi và yêu cầu nhập lại.
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        print(list(filter(lambda x: x % 2 == 0, range(m, n + 1))))
        break
    else:
        print("Điều kiện không hợp lệ. Vui lòng nhập lại.")