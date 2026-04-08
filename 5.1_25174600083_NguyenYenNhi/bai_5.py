#bai_5
"""
Nhập từ bàn phím một số tự nhiên n. Tạo một list có n phần tử từ 1 đến n. Tìm và
in ra màn hình một danh sách chứa các số nguyên tố và một danh sách chứa các
số hoàn hảo thuộc dãy đã cho.
"""

n = int(input("Nhập một số tự nhiên n: "))
a = list(range(1, n + 1))
so_nguyen_to = []
so_hoan_hao = []
for i in a:
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            so_nguyen_to.append(i)
print("Số nguyên tố trong danh sách là :",so_nguyen_to)

tong_uoc = 0
for i in range(1, j):
    if j % i == 0:
        tong_uoc += i
if tong_uoc == j and j != 0:
    so_hoan_hao.append(j)
print("Số hoàn hảo trong danh sách là :",so_hoan_hao)