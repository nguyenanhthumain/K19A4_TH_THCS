ID_DUNG = "hocsinh"
PASS_DUNG = "123456"
while True:
    id = input("Nhập ID: ")
    password = input("Nhập password: ")
    if id == ID_DUNG and password == PASS_DUNG:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai ID hoặc password, yêu cầu nhập lại!")