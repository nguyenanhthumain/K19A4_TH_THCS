"""Bài 9: Viết chương trình nhập ID và password. Chương trình sẽ lặp lại việc nhập. Viết chương trình nhập ID và password. Chương trình sẽ lặp lại việc nhập ID và password đến khi user nhập đúng. Thao tác nhập được thực hiện ít
nhất 1 lần."""
id = "leducloc"
password = "25174600220"
while True:  
    id = input("Nhập ID: ")
    password = input("Nhập password: ")
    if id == id and password == password:
        print("Đăng nhập thành công!")
        break  
    else:
        print("ID hoặc password không đúng. Vui lòng thử lại.")