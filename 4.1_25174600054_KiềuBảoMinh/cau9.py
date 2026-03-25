ID_dung = "admin"
PASS_dung = "123"
while True:
    id = input("Nhập ID: ")
    password = input("Nhập password: ")   
    if id == ID_dung and password == PASS_dung:
        print("Đăng nhập thành công")
        break
    else:
        print("Sai ID hoặc password, nhập lại!")