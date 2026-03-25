# bai_5
"""Viết chương trình tìm bội chung nhỏ nhất của hai số nguyên được nhập từ bàn
phím thông qua giải thuật Euclide:
• Tính UCLN của a và b bằng cách sử dụng giải thuật Euclid.
• Sau khi tìm được UCLN(a, b), tính BCNN của a và b qua công thức:

BCNN(a, b) =

(a × b)
UCLN(a, b)
"""

# for
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if a <= 0 or b <= 0 or a % 1 != 0 or b % 1 != 0 :
    print("Yêu cầu nhập lại")
else :
    for i in range(1000000000) :
        if a % i == 0 and b % i == 0 :
            ucln = i
    bcnn = (a * b) / ucln
    print("Bội chung nhỏ nhất của a và b là: ", bcnn)
# while
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))    
if a <= 0 or b <= 0 or a % 1 != 0 or b % 1 != 0 :
    print("Yêu cầu nhập lại")   
else :
    i = 1
    while i <= min(a, b) :
        if a % i == 0 and b % i == 0 :
            ucln = i
        i += 1
    bcnn = (a * b) / ucln
    print("Bội chung nhỏ nhất của a và b là: ", bcnn)