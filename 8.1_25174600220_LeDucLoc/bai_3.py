"""Bài 3:
a) Viết chương trình (yêu cầu xây dựng hàm) để nhập số nguyên dương n từ bàn
phím. Kiểm tra n có phải là số nguyên tố không?
b) Viết chương trình, trong đó xây dựng hàm nhập số nguyên dương n từ bàn
phím. Kiểm tra n có phải là số hoàn hảo không?
c) Trong toán học số nguyên n gọi là số đối xứng nếu đọc từ trái qua phải, hay từ
phải qua trái đều được số giống nhau. Ví dụ: 11, 121, 101 là các số đối xứng.

Viết chương trình (yêu cầu xây dựng hàm) in ra màn hình các số đối xứng trong
phạm vị 1000. Quy cách in mỗi số đối xứng chiếm 05 ký tự và tối đa 15 số trên
một hàng mới chuyển qua hàng mới."""

#a
n = int(input("Nhập số nguyên dương n: "))
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

#b
n = int(input("Nhập số nguyên dương n: "))
def kiem_tra_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
if kiem_tra_so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")

#c
def kiem_tra_so_doi_xung(n):
    str_n = str(n)
    return str_n == str_n[::-1]     
def in_so_doi_xung():
    count = 0
    for i in range(1000):
        if kiem_tra_so_doi_xung(i):
            print(f"{i:05}", end=' ')
            count += 1
            if count % 15 == 0:
                print() 
in_so_doi_xung()        
