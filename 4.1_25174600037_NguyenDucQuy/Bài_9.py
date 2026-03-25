while True:
    id = input("Nhập ID: ")
    pw = input("Nhập password: ")

    if id == "admin" and pw == "123":
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai rồi, nhập lại!")