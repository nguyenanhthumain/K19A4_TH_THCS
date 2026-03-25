# Bài 2:
"""
Viết chương trình tìm ước chung lớn nhất của 2 số nguyên m và n. Gợi ý:
 Áp dụng thuật toán Euclide bằng cách liên tiếp lấy số lớn trừ đi số nhỏ, khi nào 2 số bằng nhau thì đó là UCLN.
 Trong chương trình, ta quy ước m là số lớn và n là số nhỏ. Thêm biến phụ r để tính hiệu của 2 số. Sau đó đặt lại m hoặc n bằng r sao
cho m > n và lặp lại. Vòng lặp dừng khi m = n
"""

m = int(input("Nhập số nguyên dương m : "))
n = int(input("Nhập số nguyên dương n : "))  
if m < 0 or n < 0  or m < n or m == n :
    print("Yêu cầu nhập lại.")
else :
    while m != n :
        if m - n > 0 :
            m = m - n
        else :
            n = n -m 
    print("Ước chung lớn nhất của m và n là : ", m)