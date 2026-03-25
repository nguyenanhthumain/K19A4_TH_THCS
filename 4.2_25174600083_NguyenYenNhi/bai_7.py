# bai_7
"""Viết chương trình gọi đồ uống. Giả sử menu của chúng ta có các loại thức
uống như sau:
1. Cafe
2. Cam vắt
3. Nước ép cà rốt
4. Nước lọc
5. Nước dừa
"""
# for
print("Menu: \n1. Cafe \n2. Cam vắt \n3. Nước ép cà rốt \n4. Nước lọc \n5. Nước dừa")
chon = int(input("Nhập lựa chọn của bạn: "))
for i in range(1 , 6) :
    if chon == 1 :
        print("Bạn đã chọn Cafe")
        break
    elif chon == 2 :
        print("Bạn đã chọn Cam vắt")
        break
    elif chon == 3 :
        print("Bạn đã chọn Nước ép cà rốt")
        break
    elif chon == 4 :
        print("Bạn đã chọn Nước lọc")
        break
    elif chon == 5 :
        print("Bạn đã chọn Nước dừa")
        break
    else :
        print("Yêu cầu nhập lại")

# while
print("Menu: \n1. Cafe \n2. Cam vắt \n3. Nước ép cà rốt \n4. Nước lọc \n5. Nước dừa")
chon = int(input("Nhập lựa chọn của bạn: "))    
while True :
    if chon == 1 :
        print("Bạn đã chọn Cafe")
        break
    elif chon == 2 :
        print("Bạn đã chọn Cam vắt")
        break
    elif chon == 3 :
        print("Bạn đã chọn Nước ép cà rốt")
        break
    elif chon == 4 :
        print("Bạn đã chọn Nước lọc")
        break
    elif chon == 5 :
        print("Bạn đã chọn Nước dừa")
        break
    else :
        print("Yêu cầu nhập lại")