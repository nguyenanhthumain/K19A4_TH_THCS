#bai_3
"""
a) Viết chương trình (yêu cầu xây dựng hàm) để nhập số nguyên dương n từ bàn
phím. Kiểm tra n có phải là số nguyên tố không?
b) Viết chương trình, trong đó xây dựng hàm nhập số nguyên dương n từ bàn
phím. Kiểm tra n có phải là số hoàn hảo không?
c) Trong toán học số nguyên n gọi là số đối xứng nếu đọc từ trái qua phải, hay từ
phải qua trái đều được số giống nhau. Ví dụ: 11, 121, 101 là các số đối xứng.

Viết chương trình (yêu cầu xây dựng hàm) in ra màn hình các số đối xứng trong
phạm vị 1000. Quy cách in mỗi số đối xứng chiếm 05 ký tự và tối đa 15 số trên
một hàng mới chuyển qua hàng mới.
"""

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n : "))
if so_nguyen_to(n) and n > 0 :
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

def so_hoan_hao(n):
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n
n = int(input("Nhập n : "))
if so_hoan_hao(n) and n > 0:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")

def so_doi_xung(n):
    return str(n) == str(n)[::-1]
a = 0
for i in range(1001):
    if so_doi_xung(i):
        print(f"{i:05}", end=' ')
        a += 1
        if a % 15 == 0:
            print()