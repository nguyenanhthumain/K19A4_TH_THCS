# bai_6
"""Bài 6:
Viết chương trình nhập vào một số từ bàn phím có giá trị >100, hãy tính tổng
các chữ số của số vừa nhập rồi hiển thị kết quả."""
# for
a = int(input("Nhập một số có giá trị > 100: "))
if a <= 100 :
    print("Yêu cầu nhập lại")
else :
    tong = 0 
    for i in str(a) :
        tong = tong + int(i)    
    print("Tổng các chữ số của số vừa nhập là: ", tong)

# while
a = int(input("Nhập một số có giá trị > 100: "))
if a <= 100 :   
    print("Yêu cầu nhập lại")
else :
    tong = 0
    while a > 0 :
        tong = tong + a % 10
        a = a // 10
    print("Tổng các chữ số của số vừa nhập là: ", tong)