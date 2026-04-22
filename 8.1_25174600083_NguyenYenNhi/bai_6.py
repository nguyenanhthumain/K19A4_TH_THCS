#bai_6
"""
Viết chương trình đề in ra màn hình số kế tiếp của số nguyên được người
dùng nhập vào từ bàn phím. Hướng dẫn: Định nghĩa một hàm value(x) để tính
số kế tiếp của số bạn vừa nhập và sử dụng lệnh count để in ra màn hình kết quả.
"""

a = int(input("Nhập một số nguyên: "))
def value(x):
    return x + 1
print(f"Số kế tiếp của {a} là: {value(a)}")