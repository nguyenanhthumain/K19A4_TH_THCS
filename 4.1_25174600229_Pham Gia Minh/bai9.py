id_dung = "sinhvien"
pw_dung = "k19"

while True:
    u = input("Username: ")
    p = input("Password: ")
    if u == id_dung and p == pw_dung:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Sai roi, nhap lai di!")