"""Viết chương trình tìm ước chung lớn nhất của 2 số nguyên m và n. 
Gợi ý:
Áp dụng thuật toán Euclide bằng cách liên tiếp lấy số lớn trừ đi số nhỏ, khi nào 2 số bằng nhau thì đó là UCLN.
Trong chương trình, ta quy ước m là số lớn và n là số nhỏ. Thêm biến phụ r để tính hiệu của 2 số. Sau đó đặt lại m hoặc n bằng r sao cho m > n và lặp lại. Vòng lặp dừng khi m = n"""

m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))        
if m > 0 and n > 0:               
    while m != n:                      
        r = m - n                         
        if r > 0:                         
            m = r                         
        else:                              
            n = -r                        
    print("Ước chung lớn nhất của", m, "và", n, "là:", m)
else:
    print("Vui lòng nhập hai số nguyên dương.")
