# Bài 9:
"""
Viết chương trình nhập ID và password. Chương trình sẽ lặp lại việc nhập
ID và password đến khi user nhập đúng. Thao tác nhập được thực hiện ít
nhất 1 lần.
"""
ID = "25174600083"
PASSWORD = "NGUYEN_YEN_NHI-DHKL19A4HN"      
id = input("Nhập ID : ")
password = input("Nhập password : ")
if id == ID and password == PASSWORD :
    print("Đăng nhập thành công.")
else :
    print("Yêu cầu nhập lại .")