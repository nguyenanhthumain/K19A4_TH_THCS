"""Bài 6: Viết chương trình đề in ra màn hình số kế tiếp của số nguyên được người
dùng nhập vào từ bàn phím. Hướng dẫn: Định nghĩa một hàm value(x) để tính
số kế tiếp của số bạn vừa nhập và sử dụng lệnh count để in ra màn hình kết quả."""


def value(x):
    return x + 1

x = int(input("Nhập một số nguyên: "))
print(f"Số kế tiếp của {x} là: {value(x)}")