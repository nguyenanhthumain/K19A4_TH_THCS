# bai_2
"""
Viết chương trình nhập vào từ bàn phím tử số và mẫu số của một phân số, nếu
mẫu số là 0 thì nhập lại.
"""
#for 
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
for i in range(1 , mau+1):
    if mau == 0 :
        print("Yêu cầu nhập lại")
    else :
        print("Phân số là: ", tu , "/" , mau)
        break