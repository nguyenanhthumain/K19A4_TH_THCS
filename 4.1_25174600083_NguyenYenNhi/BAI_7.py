# Bài 7:
"""
Viết chương trình hiển thị một menu các chức năng của phép toán (cộng,trừ, nhân, chia) 
giữa hai số cho người dùng chọn, bấm số 0 để thoát.
"""

print("   MENU  \n1. Cộng hai số \n2. Trừ hai số \n3. Nhân hai số \n4. Chia hai số \n0. Thoát")
a = float(input("Nhập số thứ nhất : "))
b = float(input("Nhập số thứ hai : "))  
chon = int(input("Chọn : "))
if chon == 1 :
    print("Tổng của a và b là : ", a + b)
elif chon == 2 :
    print("Hiệu của a và b là : ", a - b)       
elif chon == 3 :
    print("Tích của a và b là : ", a * b)
elif chon == 4 and b != 0 :
    print("Thương của a và b là : ", a / b)
else : 
    print("Thoát chương trình.")