ID = "deptrai"
PASSWORD = "123456"

while True:
    id = input("Nhập ID: ")
    pw = input("Nhập password: ")

    if id == ID and pw == PASSWORD:
        print("Đăng nhập thành công")
        break
    else:
        print("Yêu cầu nhập lại")