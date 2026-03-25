ID_DUNG   = "admin"
PASS_DUNG = "123456"
so_lan    = 0
 
while True:
    so_lan += 1
    user_id = input("Nhập ID: ")
    user_pw = input("Nhập Password: ")
 
    if user_id == ID_DUNG and user_pw == PASS_DUNG:
        print(f"Đăng nhập thành công! (Số lần thử: {so_lan})")
        break
    else:
        print("ID hoặc Password không đúng. Vui lòng thử lại.")