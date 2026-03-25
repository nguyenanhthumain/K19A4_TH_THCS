ID = "Thu"
Password ="1123"
while True:
    id = input("Nhập ID:")
    mat_khau =input("Nhập mật khẩu password:")
    if id == ID and mat_khau == Password:
        print(f"Đã đang nhập thành công")
        break
    else:
        print(f"Yêu cầu nhập lại")
