#bai_4
"""
Tạo một list có 100 số tự nhiên đầu tiên với bước nhảy là 2 nằm trong đoạn từ m
đến n với 0 < m < n được nhập từ bàn phím. Tính tổng của chúng và đưa kết quả
ra màn hình.
"""

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
List = []
while len(List) < 100 and m < n:
    List.append(m)
    m += 2
tong = 0
for i in List :
    tong += i 
print("Danh sách các số tự nhiên là :", List)
print("Tổng của chúng là : ",tong)