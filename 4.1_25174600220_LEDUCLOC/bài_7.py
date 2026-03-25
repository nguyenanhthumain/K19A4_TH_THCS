"""Bài 7: Viết chương trình hiển thị một menu các chức năng của phép toán (cộng,
trừ, nhân, chia) giữa hai số cho người dùng chọn, bấm số 0 để thoát."""

from secrets import choice


print("Menu:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")
while True:
    a = input("Chọn chức năng (1-4) hoặc 0 để thoát: ")
    if a == '0':
        print("Thoát chương trình.")
        break
    elif a in ['1', '2', '3', '4']:
        b = float(input("Nhập số thứ nhất: "))
        c = float(input("Nhập số thứ hai: "))
        if a == '1':
            f = b + c
            print("Kết quả:", f)
        elif a == '2':
            f = b - c
            print("Kết quả:", f)
        elif a == '3':
            f = b * c
            print("Kết quả:", f)
        elif a == '4':
            if c != 0:
                f = b / c
                print("Kết quả:", f)
            else:
                print("Lỗi: Không thể chia cho 0.")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")