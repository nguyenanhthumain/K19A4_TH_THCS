"""Bài 4: Viết chương trình nhập n số dương từ bàn phím. Chương trình sẽ kết thúc
nếu một trong các số đó là số âm."""
n = int(input("Nhập số lượng số dương: "))
if n > 0:
    for i in range(n):
        num = int(input("Nhập số dương thứ {}: ".format(i + 1)))
        if num < 0:
            print("Số âm đã được nhập. Chương trình kết thúc.")
            break
else:
    print("Vui lòng nhập một số lượng số dương hợp lệ.")